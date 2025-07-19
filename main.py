from blockbrain.detector import run_live_detection, run_file_detection
import argparse

parser = argparse.ArgumentParser(description="blockbrain — детектор аномалий в блокчейн-транзакциях")
parser.add_argument('--live', action='store_true', help="Запуск анализа в реальном времени")
parser.add_argument('--file', type=str, help="Путь к JSON-файлу с транзакциями")

args = parser.parse_args()

if args.live:
    run_live_detection()
elif args.file:
    run_file_detection(args.file)
else:
    print("Укажите --live или --file <path>")
