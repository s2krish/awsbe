from django.core.management.base import BaseCommand, CommandError


import logging
logger = logging.getLogger('ldjango')


class Command(BaseCommand):
    help = 'Test command'

    def handle(self, *args, **options):
        logger.info("Testcron Info log")
        logger.warn("Testcron Warning log")
        logger.debug("Testcron Debug log")
        logger.error("Testcron Error log")

        