"""Regression checks for document identity and mixed-rights metadata."""
import importlib.util
from pathlib import Path
from types import SimpleNamespace
import unittest

path = Path(__file__).resolve().parents[1] / '_ext/schema_org.py'
spec = importlib.util.spec_from_file_location('schema_org', path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class MetadataTests(unittest.TestCase):
    def test_localized_identity_without_fabricated_dates_or_license(self):
        for lang in ('en', 'ko'):
            app = SimpleNamespace(config=SimpleNamespace(language=lang))
            result = module._article_entry(app, 'docs/v002/index', {'title': '<em>ISA</em> &amp; RTL'})
            self.assertEqual(result['url'], f'https://docs.pccx.ai/{lang}/docs/v002/index.html')
            self.assertEqual(result['headline'], 'ISA & RTL')
            self.assertTrue(result['license'].endswith('/pccx/blob/main/LICENSE'))
            self.assertEqual(result['publisher']['name'], 'Altifigence')
            self.assertNotIn('datePublished', result)
            self.assertNotIn('dateModified', result)
            self.assertNotIn('author', result)

    def test_explicit_page_metadata_survives(self):
        app = SimpleNamespace(config=SimpleNamespace(language='en'))
        result = module._article_entry(app, 'index', {'meta': {'author': 'A contributor', 'schema_date_published': '2026-09-27'}})
        self.assertEqual(result['author']['name'], 'A contributor')
        self.assertEqual(result['datePublished'], '2026-09-27')


if __name__ == '__main__':
    unittest.main()
