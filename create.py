from db_config import Message


def main():
    # インスタンスを作成してから保存
    message = Message(user="Bob", content="hello")
    message.save()

    # インスタンスを生成しないで保存するcreateメソッド
    def create_message():
        Message.create(user="Tom", content="Hello Bob")

    create_message()


if __name__ == "__main__":
    main()
