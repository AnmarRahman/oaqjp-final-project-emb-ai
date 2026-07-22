# Final Project Submission Guide

## Option 1 - AI-Graded Submission

Task 1 repository URL:
Paste the public GitHub URL for `README.md` after pushing the contents of this `final_project` folder to the root of your fork. The README already contains the exact required title: `Final project`.

Use the forked IBM repo URL, not a `finalProject2` repo URL:
`https://github.com/AnmarRahman/oaqjp-final-project-emb-ai/blob/main/README.md`

Task 2 Activity 1:
Submit `submission_artifacts/2a_emotion_detection.txt`.

Important: Task 2 is the early-stage code. It must show `emotion_detector` returning raw `response.text`, not the later formatted dictionary.

Task 2 Activity 2:
Submit `submission_artifacts/2b_application_creation.txt`.

Important: Task 2 terminal output should use the early root-file import:
`import emotion_detection`

Task 3 Activity 1:
Submit `submission_artifacts/3a_output_formatting.txt` or paste the code from `EmotionDetection/emotion_detection.py`.

Important: Task 3 and later use the formatted dictionary version.

Task 3 Activity 2:
Submit `submission_artifacts/3b_formatted_output_test.txt`.

Task 4 Activity 1:
Paste the public GitHub URL for `EmotionDetection/__init__.py` after pushing this project to your fork.

Use the forked IBM repo URL, not a `finalProject2` repo URL:
`https://github.com/AnmarRahman/oaqjp-final-project-emb-ai/blob/main/EmotionDetection/__init__.py`

Task 4 Activity 2:
Submit `submission_artifacts/4b_packaging_test.txt`.

Task 5 Activity 1:
Submit `submission_artifacts/5a_unit_testing.txt` or paste the code from `test_emotion_detection.py`.

Task 5 Activity 2:
Submit `submission_artifacts/5b_unit_testing_result.txt`.

Task 6 Activity 1:
Submit `submission_artifacts/6a_server.txt` or paste the code from `server.py`.

Task 6 Activity 2:
Upload `submission_artifacts/6b_deployment_test.png`.

Task 7 Activity 1:
Submit `submission_artifacts/7a_error_handling_function.txt` or paste the code from `EmotionDetection/emotion_detection.py`.

Task 7 Activity 2:
Submit `submission_artifacts/7b_error_handling_server.txt` or paste the code from `server.py`.

Task 7 Activity 3:
Upload `submission_artifacts/7c_error_handling_interface.png`.

Task 8 Activity 1:
Submit `submission_artifacts/8a_server_modified.txt` or paste the final code from `server.py`.

Task 8 Activity 2:
Submit `submission_artifacts/8b_static_code_analysis.txt`.

## Local Verification Commands

```powershell
cd "C:\Users\Anmar Abdelrahman\Desktop\finalProject2\final_project"
.\.venv\Scripts\python.exe test_emotion_detection.py
.\.venv\Scripts\python.exe server.py
.\.venv\Scripts\python.exe -m pylint --persistent=n server.py
```

## Fixes Based On The Failed Submission

- Do not submit only `Import successful` for terminal-output questions. Include the import command, function call, and printed dictionary output.
- For Task 2 Activity 1, submit the raw `response.text` version from `2a_emotion_detection.txt`; do not submit the final formatted version there.
- For Task 2 Activity 2, use `import emotion_detection`, because this is before packaging.
- For Task 2, Task 3, and Task 4 terminal outputs, the dictionary must visibly include `anger`, `disgust`, `fear`, `joy`, `sadness`, and `dominant_emotion`.
- For Task 4 Activity 2, use `from EmotionDetection.emotion_detection import emotion_detector`.
- For Task 5 Activity 1, submit the full unit-test file with all five required test statements.
- For `server.py`, use this exact import line: `from EmotionDetection.emotion_detection import emotion_detector`.
- For web screenshots, make sure the screenshot visibly shows entered text, the Run analysis action result, and the final response area.
- For the error-handling screenshot, the textarea must be visibly empty. There is no placeholder text in the regenerated `7c_error_handling_interface.png`.
- When updating GitHub, push the files inside `final_project` as the repo root contents. Do not push a nested `final_project/final_project/...` structure.
