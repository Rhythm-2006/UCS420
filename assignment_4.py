import pandas as pd

roll_number = input("Enter your college roll number: ").strip()

last_two_digits = roll_number[-2:]

categories = ["billing", "account", "general"]

fixed_entries = [
    {
        "question": "what is the annual fee",
        "answer": "The annual fee is Rs 500.",
        "keywords": "fee cost price charge",
        "category": "billing"
    },
    {
        "question": "how to reset password",
        "answer": "Go to Settings > Reset Password.",
        "keywords": "password reset login",
        "category": "account"
    },
    {
        "question": "what are your working hours",
        "answer": "We are open 9 AM to 5 PM.",
        "keywords": "hours timing open time",
        "category": "general"
    },
    {
        "question": "how can i pay the fee",
        "answer": "You can pay via UPI, card, or net banking.",
        "keywords": "pay payment upi fee",
        "category": "billing"
    }
]

personalized_entries = []

for digit in last_two_digits:
    d = int(digit)
    category = categories[d % 3]

    if category == "billing":
        entry = {
            "question": "how can i check my payment status",
            "answer": "You can check your payment status from the payment section.",
            "keywords": "payment status transaction",
            "category": "billing"
        }

    elif category == "account":
        entry = {
            "question": "how do i update my registered mobile number",
            "answer": "You can update your registered mobile number from account settings.",
            "keywords": "mobile number update account",
            "category": "account"
        }

    else:
        entry = {
            "question": "where can i find general information",
            "answer": "General information is available in the help section.",
            "keywords": "information help support",
            "category": "general"
        }

    personalized_entries.append(entry)

all_entries = fixed_entries + personalized_entries

df = pd.DataFrame(all_entries)

print("\nQ1: Final 6-row DataFrame")
print(df)


def score_query(query, df):
    query_words = query.lower().split()
    results = []

    for index, row in df.iterrows():
        text = (
            row["question"] + " " +
            row["answer"] + " " +
            row["keywords"]
        ).lower()

        score = 0

        for word in query_words:
            if word in text:
                score += 1

        if score > 0:
            results.append({
                "index": index,
                "question": row["question"],
                "answer": row["answer"],
                "category": row["category"],
                "score": score
            })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results


print("\nQ2: Query Scoring")

query = input("Enter a query: ")

results = score_query(query, df)

if len(results) == 0:
    print("No matching entries found.")
else:
    for result in results:
        print(result)


def same_category(category_name, df):
    return df[df["category"] == category_name]


category_name = personalized_entries[0]["category"]

print("\nQ3: Same Category")
print("Category:", category_name)
print(same_category(category_name, df))


print("\nQ4: Add New Keyword")

new_keyword = input("Enter a new keyword: ")

df.loc[0, "keywords"] = (
    df.loc[0, "keywords"] + " " + new_keyword
)

filename = roll_number + "_faq_data.csv"

df.to_csv(filename, index=False)

print("Updated DataFrame:")
print(df)

print("File saved as:", filename)


print("\nQ5: FAQ Entries Per Category")

category_counts = df.groupby("category").size()

print(category_counts)


def score_query_with_ties(query, df):
    query_words = query.lower().split()
    results = []

    for index, row in df.iterrows():
        text = (
            row["question"] + " " +
            row["answer"] + " " +
            row["keywords"]
        ).lower()

        score = 0

        for word in query_words:
            if word in text:
                score += 1

        if score > 0:
            results.append({
                "index": index,
                "question": row["question"],
                "answer": row["answer"],
                "category": row["category"],
                "score": score
            })

    if len(results) == 0:
        print("No matching entries found.")
        return

    highest_score = max(result["score"] for result in results)

    top_results = [
        result for result in results
        if result["score"] == highest_score
    ]

    print("Highest score:", highest_score)

    if len(top_results) > 1:
        print("Tie detected. All equally matching entries are:")
    else:
        print("Best matching entry:")

    for result in top_results:
        print("\nQuestion:", result["question"])
        print("Answer:", result["answer"])
        print("Category:", result["category"])
        print("Score:", result["score"])


print("\nQ6: Tie Demonstration")

print("\nQuery: fee")
score_query_with_ties("fee", df)

print("\nQuery: password")
score_query_with_ties("password", df)