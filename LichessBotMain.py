import requests
import json
from stockfish import Stockfish

stockfish = Stockfish('stockfish_20090216_x64_bmi2.exe', parameters={"Threads": 8, "Minimum Thinking Time": 300})
stockfish.set_depth(15)
stockfish.set_skill_level(25)

api_key = 'REPLACE_WITH_API_KEY'

headers = {'Authorization': f'Bearer {api_key}'}
game_state_url = 'https://lichess.org/api/stream/event'
game_id = 'placeholder'
is_checkmate = False
bot_challenges = False

while True:
    state_session = requests.Session()
    request = state_session.get(game_state_url, headers=headers, stream=True)
    for line in request.iter_lines():
        if len(line) == 0:
            print('Request response is empty.')
        if len(line) != 0:
            challenge_state_json = json.loads(line)
            if challenge_state_json['type'] == 'challenge':
                print('BOT_NAME has been challenged.')
                challenge_id = challenge_state_json['challenge']['id']
                challenger = challenge_state_json['challenge']['challenger']['id']
                print('Challenge ID is: ' + challenge_id + '. Challenger is: ' + challenger)
                if challenge_state_json['challenge']['variant']['key'] != 'standard':
                    requests.post('https://lichess.org/api/challenge/' + challenge_id + '/decline', params={
                    },
                                  headers={
                                      'Authorization': f'Bearer {api_key}'
                                  })
                    print('Challenge has been declined for improper variant.')
                    continue

                else:
                    requests.post('https://lichess.org/api/challenge/' + challenge_id + '/accept', params={
                    },
                                  headers={
                                      'Authorization': f'Bearer {api_key}'
                                  })

            current_move = 'placeholder'
            best_move = 'placeholder'
            position = ['placeholder', 'placeholder']
            black_position = ['placeholder', 'placeholder']
            white = True

            second_session = requests.Session()
            request = second_session.get(game_state_url, headers=headers, stream=True)

            for line in request.iter_lines():
                game_start_json = json.loads(line)
                print(game_start_json)
                game_id = game_start_json['game']['id']
                print('Game ID is: ' + game_id)
                break

            game_stream_url = 'https://lichess.org/api/bot/game/stream/' + game_id
            bot_move_url = 'https://lichess.org/api/bot/game/' + game_id + '/move/'

            s = requests.Session()
            r = s.get(game_stream_url, headers=headers, stream=True)

            i = 0
            move_count = 0

            for line in r.iter_lines():
                if line:
                    i = i + 1
                    move_count = move_count + .5
                    move_count = float(move_count)

                    if move_count.is_integer():
                        move_count = int(move_count)
                        move_count = str(move_count)
                        print('It is move ' + move_count + '.')
                        move_count = float(move_count)

                    start_json = json.loads(line)
                    if i == 1:
                        if start_json["white"]["id"] == 'REPLACE_WITH_BOT_USERNAME':
                            white = True
                            print('It is white to move. I am white.')
                        else:
                            white = False
                            print('It is white to move. I am black.')

                        if start_json['speed'] == 'bullet' and i == 1:
                            stockfish.set_depth(15)
                            stockfish.set_skill_level(20)
                        elif start_json['speed'] == 'blitz' and i == 1:
                            stockfish.set_depth(15)
                            stockfish.set_skill_level(25)
                        elif start_json['speed'] == 'rapid' and i == 1:
                            stockfish.set_depth(19)
                            stockfish.set_skill_level(30)
                        elif start_json['speed'] == 'classical' and i == 1:
                            stockfish.set_depth(20)
                            stockfish.set_skill_level(30)
                        elif start_json['speed'] == 'correspondence' and i == 1:
                            stockfish.set_depth(20)
                            stockfish.set_skill_level(30)

                    if white and i == 1:
                        position.clear()
                        stockfish.set_position()
                        best_move = stockfish.get_best_move()
                        requests.post(bot_move_url + best_move, params={
                        },
                                      headers={
                                          'Authorization': f'Bearer {api_key}'
                                      })
                        best_move = str(best_move)
                        position.append(best_move)
                        stockfish.set_position(position)

                    if not white and i == 1:
                        print('I am waiting to move.')

                    if not white and i == 2:
                        black_position.clear()
                        current_move = start_json["moves"]
                        current_move = str(current_move)
                        current_move = current_move.split()
                        current_move = current_move[-1]
                        black_position.append(current_move)

                        stockfish.set_position(black_position)
                        best_move = stockfish.get_best_move()
                        black_position.append(best_move)

                        requests.post(bot_move_url + best_move, params={
                        },
                                      headers={
                                          'Authorization': f'Bearer {api_key}'
                                      })

                    if start_json['type'] == 'gameState':
                        # If bot is white and first move has already been played
                        if not i % 2 == 0 and white and i > 1:
                            current_move = start_json["moves"]
                            current_move = str(current_move)
                            current_move = current_move.split()
                            current_move = current_move[-1]
                            position.append(current_move)

                            stockfish.set_position(position)
                            best_move = stockfish.get_best_move()
                            position.append(best_move)

                            requests.post(bot_move_url + best_move, params={
                            },
                                          headers={
                                              'Authorization': f'Bearer {api_key}'
                                          })
                        # If bot is black and first move has been played
                        if not white and i % 2 == 0 and i > 2:
                            current_move = start_json["moves"]
                            current_move = str(current_move)
                            current_move = current_move.split()
                            current_move = current_move[-1]
                            black_position.append(current_move)

                            stockfish.set_position(black_position)
                            best_move = stockfish.get_best_move()
                            black_position.append(best_move)

                            requests.post(bot_move_url + best_move, params={
                            },
                                          headers={
                                              'Authorization': f'Bearer {api_key}'
                                          })

                    else:
                        print('I am waiting to move.')
    continue
