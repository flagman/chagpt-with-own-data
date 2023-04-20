import re


class Preprocessor:
    """
    Cleans and preprocesses the corpus of data to ensure consistency and remove irrelevant information.
    """

    def preprocess(self, text: str) -> str:
        """
        Preprocess the input text.

        Args:
            text: The text to preprocess.

        Returns:
            The preprocessed text.
        """
        # Remove extra whitespaces
        text = re.sub(r"\s+", " ", text).strip()
        # Convert all characters to lowercase
        text = text.lower()
        # Split the text into sentences and remove stopwords
        sentences = [sentence.strip() for sentence in re.split(r"[.!?]", text)]
        stopwords = set(["the", "and", "a", "an", "in",
                        "of", "on", "to", "for", "with"])
        sentences = [
            " ".join([word for word in sentence.split()
                     if word not in stopwords])
            for sentence in sentences
            if len(sentence.split()) > 0
        ]
        # Return the preprocessed text
        return " ".join(sentences)
