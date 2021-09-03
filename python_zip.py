import gzip
import shutil
with open('doc_test.docx', 'rb') as f_in:
    with open('doc_test.docx.gz', 'wb') as f_out:
        with gzip.GzipFile('doc_test.docx', 'wb', fileobj=f_out) as f_out:
            shutil.copyfileobj(f_in, f_out)