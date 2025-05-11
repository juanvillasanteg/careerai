import logging

from logic.data_loader import load_and_persist_documents


def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("qdrant_loader")

    logger.info("Starting Qdrant data load and persistence...")
    try:
        index = load_and_persist_documents()
        logger.info("Successfully loaded and persisted documents to Qdrant.")
        logger.info("Index summary: %s", index)
    except Exception as e:
        logger.error("Failed to load and persist documents: %s", e, exc_info=True)


if __name__ == "__main__":
    main()
