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
            # TODO: Keep one language when coding (english or spanish not both)
            # TODO: Suggestion: use mypy, black and pylint (and maybe other linters) in order to make more code readable
            log.info("Done")
            print(f"Data {name} cargada correctamente")
        except exc.SQLAlchemyError as e:
            # Errores específicos de SQLAlchemy
            print(f"Error al cargar la data {name}: {e}")
        except Exception as e:
            # Excepciones generales
            print(f"Error inesperado: {e}")
            

if __name__ == "__main__":
    run_load()