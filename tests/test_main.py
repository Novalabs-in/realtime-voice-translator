import pytest
import main

def test_voicetranslatorpipeline_instantiation():
    # Verify that the class VoiceTranslatorPipeline is inspectable and loadable
    assert hasattr(main, 'VoiceTranslatorPipeline')

