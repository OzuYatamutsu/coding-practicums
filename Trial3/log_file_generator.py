from random import randint, choice
from time import ctime, sleep
from sys import argv
LOG_SOURCE = 'sample_syslog'
LOG_CONTENTS = []


def main(output_file='syslog_sim.log', interval_secs=2) -> None:
    """
    Creates a simulated log file, appending new lines
    to it every interval_secs.
    """
    
    global LOG_CONTENTS
    print(f"Loading sample log... {LOG_SOURCE}")
    with open(LOG_SOURCE, 'r') as f:
        LOG_CONTENTS = f.readlines() 

    print(f"Writing to log file: {output_file}")

    while True:
        with open(output_file, 'a+') as f:
            log_line = simulate_log_line()
            print(f"Writing log line: {log_line}")
            f.write(f"{log_line}")

        sleep(2)


def simulate_log_line() -> str:
    """
    Generates a log line for a random running process.
    Sources from LOG_SOURCE.
    """

    global LOG_CONTENTS

    timestamp = ctime()
    system_name = "localhost"
    log_line = choice(LOG_CONTENTS)
    return f"{timestamp} {system_name} {log_line}"


if __name__ == '__main__':
    if len(argv) >= 2:
        main(output_file=argv[1])
    else:
        main()

