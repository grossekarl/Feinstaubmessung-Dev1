from Classes.CSVDownloader import CSVDownloader
from Classes.DBImport import DBImport
from pathlib import Path
import sys

downloader = CSVDownloader(Path(__file__).parent.resolve(), str(sys.argv[1]), str(sys.argv[2]))
downloader.main()

importer = DBImport(Path(__file__).parent.resolve())
importer.main()