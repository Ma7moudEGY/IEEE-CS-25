#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>

using namespace std;

void Labyrinth(int width, int height) {
    vector<pair<int, int>> Direction = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    int xStart = -1, yStart = -1, xEnd = -1, yEnd = -1;

    vector<string> lab(height);
    for (int i = 0; i < height; ++i) {
        cin >> lab[i];

        if (lab[i].find('A') != string::npos) {
            xStart = i;
            yStart = lab[i].find('A');
        }
        if (lab[i].find('B') != string::npos) {
            xEnd = i;
            yEnd = lab[i].find('B');
        }
    }

    vector<vector<pair<int, int>>> path(height, vector<pair<int, int>>(width, {-1, -1}));
    vector<vector<bool>> visited(height, vector<bool>(width, false));

    queue<pair<int, int>> q;
    q.push({xStart, yStart});
    visited[xStart][yStart] = true;

    while (!q.empty()) {
        auto [xCurrent, yCurrent] = q.front();
        q.pop();

        for (auto [xMove, yMove] : Direction) {
            int xNew = xCurrent + xMove;
            int yNew = yCurrent + yMove;

            if (xNew >= 0 && xNew < height && yNew >= 0 && yNew < width &&
                !visited[xNew][yNew] && lab[xNew][yNew] != '#') {
                visited[xNew][yNew] = true;
                path[xNew][yNew] = {xMove, yMove};
                q.push({xNew, yNew});
            }
        }
    }

    if (!visited[xEnd][yEnd]) {
        cout << "NO" << endl;
        return;
    }

    cout << "YES" << endl;

    vector<pair<int, int>> ans;
    pair<int, int> end = {xEnd, yEnd};

    while (end != make_pair(xStart, yStart)) {
        auto mv = path[end.first][end.second];
        ans.push_back(mv);
        end = {end.first - mv.first, end.second - mv.second};
    }

    reverse(ans.begin(), ans.end());
    cout << ans.size() << endl;

    for (auto [dx, dy] : ans) {
        if (dx == 1 && dy == 0)
            cout << 'D';
        else if (dx == -1 && dy == 0)
            cout << 'U';
        else if (dx == 0 && dy == 1)
            cout << 'R';
        else if (dx == 0 && dy == -1)
            cout << 'L';
    }
    cout << endl;
}

int main() {
    int Height, Width;
    cin >> Height >> Width;

    Labyrinth(Width, Height);
    return 0;
}