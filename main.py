from paths import *
from utils import *


def main():
    df = format_null_values(read_excel_template(INPUT_PATH, INPUT_FILE_NAME))
    export_results(generate_all_pairs(df), OUTPUT_PATH, OUTPUT_FILE_NAME)


if __name__ == "__main__":
    os.chdir(INPUT_PATH)
    main()
    sys.exit()
