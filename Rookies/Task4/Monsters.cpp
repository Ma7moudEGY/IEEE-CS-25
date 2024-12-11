#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <limits>
#include <algorithm>

using namespace std;

struct Cell {
    int x, y;
};

void Labyrinth(int height, int width) {
    vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    vector<char> directionChars = {'R', 'L', 'D', 'U'};

    int startX = -1, startY = -1;
    vector<Cell> monsters;
    vector<string> lab(height);

    for (int i = 0; i < height; i++) {
        cin >> lab[i];
        for (int j = 0; j < width; j++) {
            if (lab[i][j] == 'A') {
                startX = i;
                startY = j;
            } else if (lab[i][j] == 'M') {
                monsters.push_back({i, j});
            }
        }
    }

    vector<vector<int>> monster_time(height, vector<int>(width, numeric_limits<int>::max()));
    queue<Cell> monster_queue;

    for (const auto& monster : monsters) {
        monster_time[monster.x][monster.y] = 0;
        monster_queue.push(monster);
    }

    while (!monster_queue.empty()) {
        Cell current = monster_queue.front();
        monster_queue.pop();

        for (auto [dx, dy] : directions) {
            int newX = current.x + dx;
            int newY = current.y + dy;

            if (newX >= 0 && newX < height && newY >= 0 && newY < width && lab[newX][newY] != '#' && monster_time[newX][newY] == numeric_limits<int>::max()) {
                monster_time[newX][newY] = monster_time[current.x][current.y] + 1;
                monster_queue.push({newX, newY});
            }
        }
    }

    vector<vector<bool>> visited(height, vector<bool>(width, false));
    vector<vector<Cell>> parent(height, vector<Cell>(width, {-1, -1}));
    vector<vector<int>> player_time(height, vector<int>(width, numeric_limits<int>::max()));
    queue<Cell> player_queue;

    visited[startX][startY] = true;
    player_time[startX][startY] = 0;
    player_queue.push({startX, startY});

    while (!player_queue.empty()) {
        Cell current = player_queue.front();
        player_queue.pop();

        if (current.x == 0 || current.x == height - 1 || current.y == 0 || current.y == width - 1) {
            vector<char> path;
            Cell temp = current;

            while (!(temp.x == startX && temp.y == startY)) {
                Cell prev = parent[temp.x][temp.y];
                for (int i = 0; i < 4; i++) {
                    if (prev.x + directions[i].first == temp.x && prev.y + directions[i].second == temp.y) {
                        path.push_back(directionChars[i]);
                        break;
                    }
                }
                temp = prev;
            }

            reverse(path.begin(), path.end());
            cout << "YES" << endl;
            cout << path.size() << endl;
            for (char c : path) cout << c;
            cout << endl;
            return;
        }

        for (int i = 0; i < 4; i++) {
            int newX = current.x + directions[i].first;
            int newY = current.y + directions[i].second;

            if (newX >= 0 && newX < height && newY >= 0 && newY < width && !visited[newX][newY] && lab[newX][newY] != '#' && player_time[current.x][current.y] + 1 < monster_time[newX][newY]) {
                visited[newX][newY] = true;
                parent[newX][newY] = current;
                player_time[newX][newY] = player_time[current.x][current.y] + 1;
                player_queue.push({newX, newY});
            }
        }
    }

    cout << "NO" << endl;
}

int main() {
    int height, width;
    cin >> height >> width;
    Labyrinth(height, width);
    return 0;
}
