import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from solidlsp.language_servers.csharp_language_server import CSharpLanguageServer
from solidlsp.language_servers.pyright_server import PyrightServer
from solidlsp.ls_config import Language, LanguageServerConfig
from solidlsp.ls_logger import LanguageServerLogger
from solidlsp.lsp_protocol_handler import lsp_types


def test_python():
    ls_config = LanguageServerConfig(
        code_language=Language.PYTHON,
        ignored_paths=[],
        trace_lsp_communication= False,
    )

    ls_logger = LanguageServerLogger(log_level= logging.DEBUG)


    pyright_server = PyrightServer(ls_config, logger=ls_logger, repository_root_path=("/Users/shouheihei1/Documents/GitHub/serena/"))
    pyright_server.start()

    with pyright_server.open_file("test/resources/repos/python/test_repo/custom_test/advanced_features.py"):
        param : lsp_types.DocumentDiagnosticParams = {
            "textDocument": {
                "uri": "file:///Users/shouheihei1/Documents/GitHub/serena/test/resources/repos/python/test_repo/custom_test/advanced_features.py"
            },
            "full": True,
        }
        x = pyright_server.server.send.text_document_diagnostic(param)
        print(x)

test_python()

    # Pyright, we cab use `pyright-langserver --stdio` but doesnt require pyright to be installed with npm, it will look through thr toml file

def test_c_sharp():
    ls_config = LanguageServerConfig(
        code_language=Language.CSHARP,
        ignored_paths=[],
        trace_lsp_communication=False,
    )

    ls_logger = LanguageServerLogger(log_level=logging.DEBUG)

    csharp_server = CSharpLanguageServer(ls_config, logger=ls_logger, repository_root_path=("/Users/shouheihei1/Documents/GitHub/serena/"))
    csharp_server.start()

    with csharp_server.open_file("test/resources/repos/csharp/test_repo/Program.cs"):
        param: lsp_types.DocumentDiagnosticParams = {
            "textDocument": {
                "uri": "file:///Users/shouheihei1/Documents/GitHub/serena/test/resources/repos/csharp/test_repo/Program.cs"
            },
            "full": True,
        }
        x = csharp_server.server.send.text_document_diagnostic(param)
        print(x)

test_c_sharp()
