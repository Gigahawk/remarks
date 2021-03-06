import subprocess

import fitz

# TODO: evaluate using the python API (instead of cli)
# https://github.com/jbarlow83/OCRmyPDF/blob/master/src/ocrmypdf/api.py
# https://ocrmypdf.readthedocs.io/en/latest/api.html

# https://stackoverflow.com/questions/11210104/check-if-a-program-exists-from-a-python-script
def is_tool(name):
    """Check whether `name` is on PATH and marked as executable."""

    # from whichcraft import which
    from shutil import which

    return which(name) is not None


def run_ocr(tmp_file, languages="eng"):
    cmd_args = []

    # TODO: use parallel for batch processing?
    # https://ocrmypdf.readthedocs.io/en/latest/batch.html

    cmd_args += ("ocrmypdf", tmp_file, tmp_file)  # modify in place

    # cmd_args += ("--pages", str(page_number))
    # cmd_args += ("--sidecar", sidecar_file)
    # ERROR: --pages and --sidecar are mutually exclusive

    cmd_args += ("--force-ocr",)

    if languages:
        cmd_args += ("-l", languages)

    # print(cmd_args)

    p = subprocess.run(cmd_args)
    print(f"{p}\n")

    return tmp_file
