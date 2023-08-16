import argparse
import time
import datetime

def send_metrics(interval, target, metric_names, values, test_mode, debug_mode):
    if not test_mode:
        from graphyte import init as graphyte_init, send as graphyte_send
        graphyte_init(target, interval=interval, timeout=2)

    while True:
        for value in values:
            for metric_name in metric_names:
                if test_mode:
                    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"{current_time} - Metric: {metric_name}, Value: {value}")
                else:
                    graphyte_send(metric_name, value)
                    if debug_mode:
                        print(f"Sent - Metric: {metric_name}, Value: {value}")
            time.sleep(interval)
#        if not test_mode:
#            break

def main():
    parser = argparse.ArgumentParser(description="Send values to Graphite endpoint or print to stdout")
    parser.add_argument("--interval", type=int, default=60, help="Time interval between sending metrics (in seconds)")
    parser.add_argument("--target", default="localhost", help="Graphite endpoint target")
    parser.add_argument("--metric_names", nargs="+", default=["not-set"], help="List of metric names")
    parser.add_argument("--test", action="store_true", help="Print metrics to stdout instead of sending to Graphite")
    parser.add_argument("--repeat", action="store_true", help="Repeat sending values in a loop")
    parser.add_argument("--debug", action="store_true", help="Print debug messages when metrics are sent")
    args = parser.parse_args()

    values = [1, 1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 3, 3, 3, 3, 3, 2, 1]

    send_metrics(args.interval, args.target, args.metric_names, values, args.test, args.debug)

if __name__ == "__main__":
    main()
