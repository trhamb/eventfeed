from fetcher import fetch_events
from parser import parse_response
from speech import build_speech, generate_ssml


def main():
    speech_list = build_speech((parse_response((fetch_events()))))

    for i in speech_list:
        print(i)

    print("Func test:")
    print(generate_ssml(speech_list))


if __name__ == "__main__":
    main()
