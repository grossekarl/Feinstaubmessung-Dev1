from Classes.CSVDownloader import CSVDownloader
from pathlib import Path
import sys

downloader = CSVDownloader(Path(__file__).parent.resolve(), str(sys.argv[1]), str(sys.argv[2]))
downloader.main()