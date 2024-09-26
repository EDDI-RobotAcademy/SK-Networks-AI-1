from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from backlog_review.entity.backlog_review import BacklogReview
from backlog_review.repository.backlog_review_repository import BacklogReviewRepository


class BacklogReviewRepositoryImpl(BacklogReviewRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, backlog, review):
        try:
            backlogReview = BacklogReview(backlog=backlog, review=review)
            backlogReview.save()

            return backlogReview

        except IntegrityError:
            return None

    def modify(self, backlog, review):
        try:
            backlogReview = BacklogReview.objects.get(backlog=backlog)

            backlogReview.review = review
            backlogReview.save()
            return backlogReview

        except ObjectDoesNotExist:
            raise ValueError(f"No backlog domain found for backlog ID {backlog.id}")

        except Exception as e:
            print(f"Error updating backlog status: {e}")
            raise e
