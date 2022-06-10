from email import message
from aiogram import Bot, Dispatcher, executor, types
from pytube import YouTube
from tkinter import *
from tkinter import messagebox
 
API_TOKEN = '5492450826:AAE4O9eRLLJAiZHype5RRsaJTjddCMcFl68'
 
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nДля того чтобы скачать видео с YouTube нажми на: \n/download")

@dp.message_handler(commands=['download'])
async def process_help_command(message: types.Message):
    await message.reply("Приступаю к подготовке данных.")
    await message.reply("Введите ссылку для скачивания видео:")

@dp.message_handler()
async def link(message: types.Message):
    # В переменной msg.text
    # содержится текст сообщения
    yt_obj=message.from_user.id
    await bot.send_message(message.from_user.id, "Ссылка для скачивания задана.")
def clicked():
    global txt1,txt2,txt3
    link=txt1.get()
    path=txt2.get()
    nm=txt3.get()
    nm+='.mp4'
    try:
        yt_obj=YouTube(link)

        filters=yt_obj.streams.filter(progressive=True, file_extension='mp4')

        filters.get_highest_resolution().download(output_path=path, filename=nm)
        messagebox.showinfo('Видео загружено!')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)