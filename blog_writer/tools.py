from crewai_tools import YoutubeChannelSearchTool
from embedchain.embedder.huggingface import HuggingFaceEmbedder
from embedchain.config import AppConfig

# Proper AppConfig with embedder config
config = AppConfig(
    embedder_config={
        "provider": "huggingface",
        "config": {
            "model": "sentence-transformers/all-MiniLM-L6-v2",
            "model_kwargs": {"device": "cpu"}
        }
    }
)

# Create HuggingFaceEmbedder with AppConfig
custom_embedder = HuggingFaceEmbedder(config=config)

# Create YouTube tool with custom embedder
yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle="@codebasics",
    config={"embedder": custom_embedder}
)
