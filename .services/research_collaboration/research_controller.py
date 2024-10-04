from flask import Flask, request, jsonify
from research_service import ResearchService

app = Flask(__name__)

research_service = ResearchService()

@app.route('/research/studies', methods=['GET'])
def get_studies():
    studies = research_service.get_studies()
    return jsonify([study.to_dict() for study in studies])

@app.route('/research/studies', methods=['POST'])
def create_study():
    study_data = request.get_json()
    study = Study(**study_data)
    research_service.add_study(study)
    return jsonify(study.to_dict()), 201

@app.route('/research/studies/<int:study_id>', methods=['GET'])
def get_study(study_id: int):
    study = research_service.get_study(study_id)
    if study:
        return jsonify(study.to_dict())
    else:
        return jsonify({'error': 'Study not found'}), 404

@app.route('/research/studies/<int:study_id>', methods=['PUT'])
def update_study(study_id: int):
    study_data = request.get_json()
    study = research_service.get_study(study_id)
    if study:
        research_service.update_study(study_id, Study(**study_data))
        return jsonify(study.to_dict())
    else:
        return jsonify({'error': 'Study not found'}), 404

@app.route('/research/studies/<int:study_id>', methods=['DELETE'])
def delete_study(study_id: int):
    research_service.delete_study(study_id)
    return jsonify({'message': 'Study deleted'}), 200

@app.route('/research/studies/<int:study_id>/collaborate', methods=['POST'])
def collaborate(study_id: int):
    collaborator_id = request.get_json()['collaborator_id']
    research_service.collaborate(study_id, collaborator_id)
    return jsonify({'message': 'Collaboration successful'}), 200

@app.route('/research/studies/<int:study_id>/share-results', methods=['POST'])
def share_results(study_id: int):
    results = request.get_json()['results']
    research_service.share_results(study_id, results)
    return jsonify({'message': 'Results shared successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
