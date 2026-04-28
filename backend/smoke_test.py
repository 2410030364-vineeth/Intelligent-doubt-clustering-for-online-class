from datetime import UTC, datetime

from app.database import close_mongo_connection, connect_to_mongo
from app.models import AskRequest
from app.routes.ask import add_doubt
from app.routes.clusters import get_clusters


def main() -> None:
    class_id = "codex_smoke_" + datetime.now(UTC).strftime("%Y%m%d%H%M%S")
    questions = [
        "Why is quicksort faster than bubble sort for large arrays?",
        "How does quick sort choose a pivot and sort arrays quickly?",
        "What is polymorphism in object oriented programming?",
        "Can you explain method overriding and polymorphism in OOP?",
        "Why do neural networks use activation functions?",
    ]

    connect_to_mongo()
    try:
        print(f"CLASS_ID={class_id}")
        for text in questions:
            response = add_doubt(AskRequest(question=text, class_id=class_id))
            print("ASK:", text)
            if response.similar_questions:
                for item in response.similar_questions:
                    print(f"  SIMILAR {item.similarity_percent}% | cluster={item.cluster} | {item.question}")
            else:
                print("  SIMILAR none - first question in class")

        clusters = get_clusters(class_id)
        print(f"TOTAL_QUESTIONS={clusters.total_questions}")
        print("MOST_ASKED_TOPICS=", clusters.most_asked_topics)
        for cluster in clusters.clusters:
            print(f"CLUSTER {cluster.cluster}: {cluster.name} | count={cluster.count} | repeated={cluster.repeated}")
            for question in cluster.questions:
                print(f"  - {question.question}")
    finally:
        close_mongo_connection()


if __name__ == "__main__":
    main()
