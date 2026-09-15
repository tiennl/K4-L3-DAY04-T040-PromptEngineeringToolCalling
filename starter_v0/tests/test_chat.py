import json
import tempfile
import unittest
from pathlib import Path

from chat import execute_tool_call, format_tool_event, run_model_tool_loop, write_transcript
from providers.base import ModelResponse, ToolCall


class ChatUiTests(unittest.TestCase):
    def test_format_tool_event_shows_input_result_and_error(self):
        rendered = format_tool_event(
            {
                "tool": "check_service_status",
                "args": {"service": "vpn"},
                "result": {"error": "not_found", "message": "VPN is unknown"},
            }
        )

        self.assertIn("check_service_status", rendered)
        self.assertIn('"service": "vpn"', rendered)
        self.assertIn("not_found", rendered)
        self.assertIn("VPN is unknown", rendered)

    def test_tool_loop_and_transcript_preserve_visible_event_details(self):
        class FakeProvider:
            def __init__(self):
                self.calls = 0

            def complete(self, messages, tools, *, model=None, temperature=0.0, tool_choice=None):
                self.calls += 1
                if self.calls == 1:
                    return ModelResponse(tool_calls=[ToolCall("inspect_device", {"asset_id": "LT-204", "check": "vpn"})])
                return ModelResponse(text="VPN check complete.")

        result = run_model_tool_loop(
            provider=FakeProvider(),
            messages=[{"role": "user", "content": "Check VPN on LT-204"}],
            tools=[],
            model="offline-test",
            max_tool_rounds=2,
        )

        self.assertEqual(result["status"], "answered")
        self.assertEqual(result["tool_events"][0]["args"]["asset_id"], "LT-204")
        self.assertIn("diagnostics", result["tool_events"][0]["result"])

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "demo.transcript.json"
            write_transcript(path, {"version": "v3", "turns": [{"tool_events": result["tool_events"]}]})
            saved = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(saved["version"], "v3")
            self.assertEqual(saved["turns"][0]["tool_events"][0]["tool"], "inspect_device")

    def test_unknown_tool_is_recorded_as_error(self):
        event = execute_tool_call(ToolCall("missing_tool", {"value": "demo"}))

        self.assertEqual(event["result"]["error"], "unknown_tool")
        self.assertIn("missing_tool", format_tool_event(event))

    def test_clarification_tool_pauses_for_the_next_user_turn(self):
        class FakeProvider:
            def complete(self, messages, tools, *, model=None, temperature=0.0, tool_choice=None):
                return ModelResponse(
                    tool_calls=[ToolCall("clarify", {"question": "Which employee ID?", "response_type": "text"})]
                )

        result = run_model_tool_loop(
            provider=FakeProvider(),
            messages=[{"role": "user", "content": "Check Sales account"}],
            tools=[],
            model="offline-test",
            max_tool_rounds=2,
        )

        self.assertEqual(result["status"], "waiting_for_user")
        self.assertEqual(result["assistant_text"], "Which employee ID?")
        self.assertEqual(result["tool_events"][0]["tool"], "clarify")


if __name__ == "__main__":
    unittest.main()
