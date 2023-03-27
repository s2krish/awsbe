from django.core.management.base import BaseCommand, CommandError


import logging
logger = logging.getLogger('ldjango')


class Command(BaseCommand):
    help = 'Test command'

    def handle(self, *args, **options):
        logger.info("Info log")
        logger.warn("Warning log")
        logger.debug("Debug log")
        logger.error("Error log")

        