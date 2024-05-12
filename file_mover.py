#!/usr/bin/env python3

import os
import shutil
import logging

# Configuração básica do logging
logging.basicConfig(filename='/var/log/file_mover.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

source_dir = '/home/andre/'
dest_dir = '/home/andre/Triage/'

try:
    content = os.listdir(source_dir)
    for entry in content:
        full_path = os.path.join(source_dir, entry)
        if os.path.isfile(full_path) and not entry.startswith("."):
            try:
                shutil.move(full_path, dest_dir)
                logging.info(f"Arquivo {entry} movido com sucesso para {dest_dir}")
            except shutil.Error as e:
                logging.warning(f"Não foi possível mover {entry} para {dest_dir}: {e}")
except Exception as e:
    logging.error(f"Erro ao listar ou mover arquivos: {e}")
