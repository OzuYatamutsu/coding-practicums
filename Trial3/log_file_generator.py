from time import ctime, sleep
from sys import argv


def main(output_file='syslog_sim.log', interval_secs=2) -> None:
    """
    Creates a simulated log file, appending new lines
    to it every interval_secs.
    """

    print(f"Writing to log file: {output_file}")

    while True:
        with open(output_file, 'a+') as f:
            log_line = simulate_log_line()
            print(f"Writing log line: {log_line}")
            f.write(f"{log_line}\n")

        sleep(2)


def simulate_log_line() -> str:
    """Generates a log line for a random running process."""

    timestamp = ctime()
    system_name = "localhost"  # TODO get from system
    process_name = "log_file_generator.py"  # TODO get process from system
    process_pid = 1234  # TODO get PID from system
    message = "[ACT]:[HTTPRESPONSEPARSER]:[Error]:data=0x600007a5e8d0, code=-1009, error=(null)"  # TODO sample from event log

    return f"{timestamp} {system_name} {process_name}[{process_pid}]: {message}"


if __name__ == '__main__':
    if len(argv) >= 2:
        main(output_file=argv[1])
    else:
        main()

