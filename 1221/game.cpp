#include <iostream>
#include <string>
using namespace std;

int main() {
	cout << "���� ���� �� ������ �մϴ�. ����, ����, �� �߿��� �Է��ϼ���.";
	cout << "\n�ι̿�>>";
	string s;
	cin >> s;
	cout << "�ٸ���>>";
	string t;
	cin >> t;

	if (s == t) {
		cout << "�ι̿��� �ٸ����� �����ϴ�.";
	}
	else if (s == "����" && t == "��") {
		cout << "�ι̿��� �̰���ϴ�.";
	}
	else if (s == "����" && t == "����") {
		cout << "�ι̿��� �̰���ϴ�.";
	}
	else if (s == "��" && t == "����") {
		cout << "�ι̿��� �̰���ϴ�.";
	}
	else if (s == "����" && t == "����") {
		cout << "�ٸ����� �̰���ϴ�.";
	}
	else if (s == "����" && t == "��") {
		cout << "�ٸ����� �̰���ϴ�";
	}
	else if (s == "��" && t == "����") {
		cout << "�ٸ����� �̰���ϴ�.";
	}
}