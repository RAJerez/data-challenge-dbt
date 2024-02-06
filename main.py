from sqlalchemy import exc
import pandas as pd
from loaders import RawLoader
import logging
from cfg import paths_dict


log = logging.getLogger()


def run_load():
    for name, path in paths_dict.items():
        log.info(f"Loading {name}")
        try:
            RawLoader(table_name=name).load_table(file_path=path)
            log.info("Done")
            print(f"Data {name} loaded correctly")
        except exc.SQLAlchemyError as e:
            # SQLAlchemy Specific Errors
            print(f"Error loading data {name}: {e}")
        except Exception as e:
            # General exceptions
            print(f"Unexpected error: {e}")
            

if __name__ == "__main__":
    run_load()