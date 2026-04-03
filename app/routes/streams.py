from flask import Blueprint, jsonify, request

streams_bp = Blueprint('streams', __name__)

# In-memory storage for streams (replace with a database in production)
streams = {}

@streams_bp.route('/live', methods=['POST'])
def start_stream():
    """
    Start a live stream.
    Request JSON body should contain: {'stream_id': 'string', 'user': 'string'}
    """
    data = request.json
    if 'stream_id' not in data or 'user' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    stream_id = data['stream_id']
    user = data['user']

    if stream_id in streams:
        return jsonify({'error': 'Stream already active'}), 400

    streams[stream_id] = {'user': user, 'status': 'live'}
    return jsonify({'message': 'Stream started', 'stream_id': stream_id}), 201

@streams_bp.route('/status/<stream_id>', methods=['GET'])
def stream_status(stream_id):
    """
    Get the status of a stream.
    """
    stream = streams.get(stream_id)
    if stream:
        return jsonify({'stream_id': stream_id, 'status': stream['status']}), 200
    return jsonify({'error': 'Stream not found'}), 404

@streams_bp.route('/manage', methods=['POST'])
def manage_stream():
    """
    Manage a live stream (e.g., stop or pause).
    Request JSON body should contain: {'stream_id': 'string', 'action': 'stop|pause'}
    """
    data = request.json
    if 'stream_id' not in data or 'action' not in data:
        return jsonify({'error': 'Invalid data'}), 400

    stream_id = data['stream_id']
    action = data['action']
    
    stream = streams.get(stream_id)
    if not stream:
        return jsonify({'error': 'Stream not found'}), 404

    if action == 'stop':
        del streams[stream_id]
        return jsonify({'message': 'Stream stopped', 'stream_id': stream_id}), 200
    elif action == 'pause':
        stream['status'] = 'paused'
        return jsonify({'message': 'Stream paused', 'stream_id': stream_id}), 200
    
    return jsonify({'error': 'Invalid action'}), 400
