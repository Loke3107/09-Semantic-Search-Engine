import streamlit as st
import chromadb

client = chromadb.Client()

collection = client.get_or_create_collection(
    name="knowledge_base"
)
documents=[
        "Python is a programming language",
        "Java is used for enterprise applications",
        "Machine Learning is a subset of AI",
        "Deep Learning uses neural networks",
        "Banana is a fruit",
        "Apple is a fruit",
        "Car is a vehicle",
        "Truck is a heavy vehicle"
    ]

collection.add(
    documents=documents,
    ids=["1","2","3","4","5","6","7","8"]
)

st.title("🔍 Semantic Search Engine")

with st.expander("View the collections"):
    for doc in documents:
        st.write(f"- {doc}")

try:
    collection.add(
        documents=documents,
        ids=[str(i) for i in range(len(documents))]
    )
except:
    pass


query = st.text_input(
    "Enter your search query:"
)

if st.button("Search"):
    if not query.strip():
        st.warning("Please enter a query.")
        st.stop()

    results = collection.query(
        query_texts=[query],
        n_results=3
    )

    st.subheader("Top Results \n (Lower distance means more relevant)")

    for i, (doc, distance) in enumerate(
        zip(
            results["documents"][0],
            results["distances"][0]
        ),
        start=1
    ):

        with st.expander(
            f"Result {i} | Distance: {distance:.3f}"
        ):
            st.write(doc)

# print("Documents Stored!")

# results = collection.query(
#     query_texts=["artificial intelligence"],
#     n_results=3
# )

# print("\n Search Results: \n")

# # for doc, distance in zip(
# #     results['documents'][0],
# #     results['distances'][0]
# # ):
# #     print(f"Document: {doc} | Distance: {distance}")
# #     print("-" * 50)

# for doc in results["documents"][0]:
#     print(doc)