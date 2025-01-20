from flask import Flask, request, jsonify
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from app.config.settings import DEBUG, HOST, PORT
import os

def create_app():
    app = Flask(__name__)
    
    # Initialize LangChain components
    llm = ChatOpenAI(temperature=0.7)
    
    # Create prompt template for topic identification
    topic_template = PromptTemplate(
        input_variables=["query"],
        template="Identify the main topic of the following query and provide a brief description: {query}"
    )
    
    # Create prompt template for detailed elaboration
    elaboration_template = PromptTemplate(
        input_variables=["topic"],
        template="Provide a detailed explanation of the following topic, including key points and a summary: {topic}"
    )
    
    # Create LangChain chains
    topic_chain = LLMChain(llm=llm, prompt=topic_template)
    elaboration_chain = LLMChain(llm=llm, prompt=elaboration_template)

    @app.route("/")
    def home():
        return jsonify({"status": "healthy"})

    @app.route("/health")
    def health_check():
        return jsonify({"status": "healthy"})

    @app.route("/api/v1/version")
    def version():
        return jsonify({"version": "1.0"})

    @app.route('/analyze', methods=['POST'])
    def analyze_query():
        try:
            # Get query from request
            data = request.get_json()
            if not data or 'query' not in data:
                return jsonify({'error': 'No query provided'}), 400

            user_query = data['query']
            summary_only = data.get('summary_only', False)

            # First, identify the topic
            topic_result = topic_chain.run(user_query)

            if summary_only:
                return jsonify({
                    'topic': topic_result.strip()
                })

            # Then, get detailed elaboration
            elaboration_result = elaboration_chain.run(topic_result)

            # Return both results
            return jsonify({
                'topic': topic_result.strip(),
                'elaboration': elaboration_result.strip()
            })

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)
    