from paths import *
from utils import *


def main():
    df = read_excel_template(INPUT_FILE_NAME)
    format_null_values(df)
    emails_query_format = get_all_pairs(df)
    export_results(emails_query_format, OUTPUT_PATH, OUTPUT_FILE_NAME)


if __name__ == "__main__":
    os.chdir(INPUT_PATH)
    main()
    sys.exit()
