import os
import sys

main_txt = r'''
<html>
  <head>
    <style>
      .container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 20px;
        justify-content: center;
        align-items: center;
        max-width: 900px;
        padding: 40px;
        border-radius: 25px;
        border: 2px solid white;
        background: rgba(0, 0, 0, 0.6);
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.4);
      }
      button {
        padding: 14px 20px;
        border-radius: 12px;
        border: 1px solid rgb(61, 106, 255);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: white;
        overflow: hidden;
        transition: all 0.2s ease-in;
        white-space: nowrap;
        cursor: pointer;
      }
      .center-btn {
        grid-column: 1 / -1;
        justify-self: center;
      }
      .exit-btn {
        padding: 14px 20px;
        border-radius: 12px;
        border: 1px solid rgb(255, 61, 61);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: white;
        overflow: hidden;
        transition: all 0.2s ease-in;
        white-space: nowrap;
        cursor: pointer;
        grid-column: 1 / -1;
        justify-self: center;
      }
      .exit-btn:hover {
        background: rgb(255, 61, 61);
        box-shadow: 0 0 30px 5px rgba(255, 0, 0, 0.815);
        transition: all 0.2s ease-out;
      }
      button:hover {
        background: rgb(61, 106, 255);
        box-shadow: 0 0 30px 5px rgba(0, 142, 236, 0.815);
        transition: all 0.2s ease-out;
      }
      body {
        background-image: url('image.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        margin: 0;
        font-family: Arial, sans-serif;
      }
    </style>
  </head>
  <body>
    <div id="app" class="container">
      <button onclick="showTask1()">Задание 1</button>
      <button onclick="showTask2()">Задание 2</button>
      <button onclick="showTask3()">Задание 3</button>
      <button onclick="showTask4()">Задание 4</button>
      <button onclick="showTask5()">Задание 5</button>
      <button onclick="showTask6()">Задание 6</button>
      <button onclick="showTask7()">Задание 7</button>
      <button onclick="showTask8()">Задание 8</button>
      <button onclick="showTask9()">Задание 9</button>
      <button onclick="showTask10()">Задание 10</button>
      <button class="center-btn" onclick="showTask11()">Задание 11</button>
      <button class="exit-btn" onclick="pywebview.api.exit_app()">Выход</button>
    </div>
    <script>
      const app = document.getElementById('app');
      const originalHTML = app.innerHTML;
      async function showTask1() {
        app.style.transition = 'opacity 0.5s ease';
        app.style.opacity = '0';
        const response = await pywebview.api.get_task1_content();
        const data = JSON.parse(response);
        const style = document.createElement('style');
        style.id = 'task1-style';
        style.textContent = data.css;
        document.head.appendChild(style);
        setTimeout(() => {
          app.className = 'task-container';
          app.innerHTML = data.html;
          const script = document.createElement('script');
          script.id = 'task1-script';
          script.textContent = data.js;
          document.body.appendChild(script);
          app.style.opacity = '1';
          app.style.transition = '';
        }, 500);
      }
      async function showTask2() {
        app.style.transition = 'opacity 0.5s ease';
        app.style.opacity = '0';
        const response = await pywebview.api.get_task2_content();
        const data = JSON.parse(response);
        const style = document.createElement('style');
        style.id = 'task2-style';
        style.textContent = data.css;
        document.head.appendChild(style);
        setTimeout(() => {
          app.className = 'task-container';
          app.innerHTML = data.html;
          const script = document.createElement('script');
          script.id = 'task2-script';
          script.textContent = data.js;
          document.body.appendChild(script);
          app.style.opacity = '1';
          app.style.transition = '';
        }, 500);
      }
      async function showTask3() {
        app.style.transition = 'opacity 0.5s ease';
        app.style.opacity = '0';
        const response = await pywebview.api.get_task3_content();
        const data = JSON.parse(response);
        const style = document.createElement('style');
        style.id = 'task3-style';
        style.textContent = data.css;
        document.head.appendChild(style);
        setTimeout(() => {
          app.className = 'task-container';
          app.innerHTML = data.html;
          const script = document.createElement('script');
          script.id = 'task3-script';
          script.textContent = data.js;
          document.body.appendChild(script);
          app.style.opacity = '1';
          app.style.transition = '';
        }, 500);
      }
      async function showTask4() {
        app.style.transition = 'opacity 0.5s ease';
        app.style.opacity = '0';
        const response = await pywebview.api.get_task4_content();
        const data = JSON.parse(response);
        const style = document.createElement('style');
        style.id = 'task4-style';
        style.textContent = data.css;
        document.head.appendChild(style);
        setTimeout(() => {
          app.className = 'task-container';
          app.innerHTML = data.html;
          const script = document.createElement('script');
          script.id = 'task4-script';
          script.textContent = data.js;
          document.body.appendChild(script);
          app.style.opacity = '1';
          app.style.transition = '';
        }, 500);
      }
      async function showTask5() {
        app.style.transition = 'opacity 0.5s ease';
        app.style.opacity = '0';
        const response = await pywebview.api.get_task5_content();
        const data = JSON.parse(response);
        const style = document.createElement('style');
        style.id = 'task5-style';
        style.textContent = data.css;
        document.head.appendChild(style);
        setTimeout(() => {
          app.className = 'task-container';
          app.innerHTML = data.html;
          const script = document.createElement('script');
          script.id = 'task5-script';
          script.textContent = data.js;
          document.body.appendChild(script);
          app.style.opacity = '1';
          app.style.transition = '';
        }, 500);
      }
      async function showTask6() {
        app.style.transition = 'opacity 0.5s ease';
        app.style.opacity = '0';
        const response = await pywebview.api.get_task6_content();
        const data = JSON.parse(response);
        const style = document.createElement('style');
        style.id = 'task6-style';
        style.textContent = data.css;
        document.head.appendChild(style);
        setTimeout(() => {
          app.className = 'task-container';
          app.innerHTML = data.html;
          const script = document.createElement('script');
          script.id = 'task6-script';
          script.textContent = data.js;
          document.body.appendChild(script);
          app.style.opacity = '1';
          app.style.transition = '';
        }, 500);
      }
      async function showTask7() {
        app.style.transition = 'opacity 0.5s ease';
        app.style.opacity = '0';
        const response = await pywebview.api.get_task7_content();
        const data = JSON.parse(response);
        const style = document.createElement('style');
        style.id = 'task7-style';
        style.textContent = data.css;
        document.head.appendChild(style);
        setTimeout(() => {
          app.className = 'task-container';
          app.innerHTML = data.html;
          const script = document.createElement('script');
          script.id = 'task7-script';
          script.textContent = data.js;
          document.body.appendChild(script);
          app.style.opacity = '1';
          app.style.transition = '';
        }, 500);
      }
      async function showTask8() {
        app.style.transition = 'opacity 0.5s ease';
        app.style.opacity = '0';
        const response = await pywebview.api.get_task8_content();
        const data = JSON.parse(response);
        const style = document.createElement('style');
        style.id = 'task8-style';
        style.textContent = data.css;
        document.head.appendChild(style);
        setTimeout(() => {
          app.className = 'task-container';
          app.innerHTML = data.html;
          const script = document.createElement('script');
          script.id = 'task8-script';
          script.textContent = data.js;
          document.body.appendChild(script);
          app.style.opacity = '1';
          app.style.transition = '';
        }, 500);
      }
      async function showTask9() {
        app.style.transition = 'opacity 0.5s ease';
        app.style.opacity = '0';
        const response = await pywebview.api.get_task9_content();
        const data = JSON.parse(response);
        const style = document.createElement('style');
        style.id = 'task9-style';
        style.textContent = data.css;
        document.head.appendChild(style);
        setTimeout(() => {
          app.className = 'task-container';
          app.innerHTML = data.html;
          const script = document.createElement('script');
          script.id = 'task9-script';
          script.textContent = data.js;
          document.body.appendChild(script);
          app.style.opacity = '1';
          app.style.transition = '';
        }, 500);
      }
      async function showTask10() {
        app.style.transition = 'opacity 0.5s ease';
        app.style.opacity = '0';
        const response = await pywebview.api.get_task10_content();
        const data = JSON.parse(response);
        const style = document.createElement('style');
        style.id = 'task10-style';
        style.textContent = data.css;
        document.head.appendChild(style);
        setTimeout(() => {
          app.className = 'task-container';
          app.innerHTML = data.html;
          const script = document.createElement('script');
          script.id = 'task10-script';
          script.textContent = data.js;
          document.body.appendChild(script);
          app.style.opacity = '1';
          app.style.transition = '';
        }, 500);
      }
      async function showTask11() {
        app.style.transition = 'opacity 0.5s ease';
        app.style.opacity = '0';
        const response = await pywebview.api.get_task11_content();
        const data = JSON.parse(response);
        const style = document.createElement('style');
        style.id = 'task11-style';
        style.textContent = data.css;
        document.head.appendChild(style);
        setTimeout(() => {
          app.className = 'task-container';
          app.innerHTML = data.html;
          const script = document.createElement('script');
          script.id = 'task11-script';
          script.textContent = data.js;
          document.body.appendChild(script);
          app.style.opacity = '1';
          app.style.transition = '';
        }, 500);
      }
    </script>
  </body>
</html>
'''

main_py = r'''
import webview
import os
import json
import re
from collections import deque

class Api:
    def get_task1_content(self):
        try:
            with open('task1.txt', 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if content.startswith('{') and '"' in content:
                data = json.loads(content)
                return json.dumps(data)
            else:
                css_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                css = css_match.group(1).strip() if css_match else ''
                js_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                js = js_match.group(1).strip() if js_match else ''
                app_match = re.search(r'<div id="app"[^>]*>(.*?)</div>', content, re.DOTALL)
                if app_match:
                    html = app_match.group(1).strip()
                else:
                    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                    body_html = body_match.group(1).strip() if body_match else content
                    body_html = re.sub(r'<style[^>]*>.*?</style>', '', body_html, flags=re.DOTALL)
                    body_html = re.sub(r'<script[^>]*>.*?</script>', '', body_html, flags=re.DOTALL)
                    html = body_html
                data = {
                    "css": css,
                    "html": html,
                    "js": js
                }
                return json.dumps(data)
        except Exception as e:
            return json.dumps({
                "css": "",
                "html": f"<h3 style='color:red'>Ошибка загрузки task1: {str(e)}</h3>",
                "js": ""
            })

    def compute_task1(self, data_str):
        data = json.loads(data_str)
        cards = data['cards']
        if not cards:
            return json.dumps({'error': 'Нет данных для обработки.'})
        max_val = max(cards)
        new_cards = [c for c in cards if c != max_val]
        old_list = ', '.join(map(str, cards))
        new_list = ', '.join(map(str, new_cards))
        return json.dumps({'old_list': old_list, 'new_list': new_list})

    def get_task1_result_content(self, compute_data_str):
        compute_data = json.loads(compute_data_str)
        try:
            with open('task1_result.txt', 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if content.startswith('{') and '"' in content:
                result_data = json.load(f)
                html = result_data['html'].format(
                    old_list=compute_data['old_list'],
                    new_list=compute_data['new_list']
                )
                return json.dumps({
                    'css': result_data['css'],
                    'html': html,
                    'js': result_data['js']
                })
            else:
                css_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                css = css_match.group(1).strip() if css_match else ''
                js_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                js = js_match.group(1).strip() if js_match else ''
                body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                body_template = body_match.group(1).strip() if body_match else content
                body_template = re.sub(r'<style[^>]*>.*?</style>', '', body_template, flags=re.DOTALL)
                body_template = re.sub(r'<script[^>]*>.*?</script>', '', body_template, flags=re.DOTALL)
                html = body_template.format(
                    old_list=compute_data['old_list'],
                    new_list=compute_data['new_list']
                )
                return json.dumps({
                    'css': css,
                    'html': html,
                    'js': js
                })
        except Exception as e:
            return json.dumps({
                'css': '',
                'html': f"<h3 style='color:red'>Ошибка загрузки результата: {str(e)}</h3>",
                'js': ''
            })

    def get_task2_content(self):
        try:
            with open('task2.txt', 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if content.startswith('{') and '"' in content:
                data = json.loads(content)
                return json.dumps(data)
            else:
                css_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                css = css_match.group(1).strip() if css_match else ''
                js_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                js = js_match.group(1).strip() if js_match else ''
                app_match = re.search(r'<div id="app"[^>]*>(.*?)</div>', content, re.DOTALL)
                if app_match:
                    html = app_match.group(1).strip()
                else:
                    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                    body_html = body_match.group(1).strip() if body_match else content
                    body_html = re.sub(r'<style[^>]*>.*?</style>', '', body_html, flags=re.DOTALL)
                    body_html = re.sub(r'<script[^>]*>.*?</script>', '', body_html, flags=re.DOTALL)
                    html = body_html
                data = {
                    "css": css,
                    "html": html,
                    "js": js
                }
                return json.dumps(data)
        except Exception as e:
            return json.dumps({
                "css": "",
                "html": f"<h3 style='color:red'>Ошибка загрузки task2: {str(e)}</h3>",
                "js": ""
            })

    def compute_task2(self, data_str):
        data = json.loads(data_str)
        films = data['films']
        if not films:
            return json.dumps({'error': 'Нет данных для обработки.'})
        predefined_films = [
            'Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон',
            'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня'
        ]
        favorites = [f for f in films if f in predefined_films]
        invalid = [f for f in films if f not in predefined_films]
        favorites_str = ', '.join(favorites) if favorites else 'Пусто'
        invalid_str = ', '.join(invalid) if invalid else 'Нет'
        return json.dumps({'favorites': favorites_str, 'invalid': invalid_str})

    def get_task2_result_content(self, compute_data_str):
        compute_data = json.loads(compute_data_str)
        try:
            with open('task2_result.txt', 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if content.startswith('{') and '"' in content:
                result_data = json.load(f)
                html = result_data['html'].format(
                    favorites=compute_data['favorites'],
                    invalid=compute_data['invalid']
                )
                return json.dumps({
                    'css': result_data['css'],
                    'html': html,
                    'js': result_data['js']
                })
            else:
                css_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                css = css_match.group(1).strip() if css_match else ''
                js_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                js = js_match.group(1).strip() if js_match else ''
                body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                body_template = body_match.group(1).strip() if body_match else content
                body_template = re.sub(r'<style[^>]*>.*?</style>', '', body_template, flags=re.DOTALL)
                body_template = re.sub(r'<script[^>]*>.*?</script>', '', body_template, flags=re.DOTALL)
                html = body_template.format(
                    favorites=compute_data['favorites'],
                    invalid=compute_data['invalid']
                )
                return json.dumps({
                    'css': css,
                    'html': html,
                    'js': js
                })
        except Exception as e:
            return json.dumps({
                'css': '',
                'html': f"<h3 style='color:red'>Ошибка загрузки результата: {str(e)}</h3>",
                'js': ''
            })

    def get_task3_content(self):
        try:
            with open('task3.txt', 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if content.startswith('{') and '"' in content:
                data = json.loads(content)
                return json.dumps(data)
            else:
                css_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                css = css_match.group(1).strip() if css_match else ''
                js_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                js = js_match.group(1).strip() if js_match else ''
                app_match = re.search(r'<div id="app"[^>]*>(.*?)</div>', content, re.DOTALL)
                if app_match:
                    html = app_match.group(1).strip()
                else:
                    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                    body_html = body_match.group(1).strip() if body_match else content
                    body_html = re.sub(r'<style[^>]*>.*?</style>', '', body_html, flags=re.DOTALL)
                    body_html = re.sub(r'<script[^>]*>.*?</script>', '', body_html, flags=re.DOTALL)
                    html = body_html
                data = {
                    "css": css,
                    "html": html,
                    "js": js
                }
                return json.dumps(data)
        except Exception as e:
            return json.dumps({
                "css": "",
                "html": f"<h3 style='color:red'>Ошибка загрузки task3: {str(e)}</h3>",
                "js": ""
            })

    def compute_task3(self, data_str):
        data = json.loads(data_str)
        nums = data['nums']
        k = data['k']
        if not nums:
            return json.dumps({'error': 'Нет данных для обработки.'})
        n = len(nums)
        k = k % n
        shifted = nums[-k:] + nums[:-k]
        old_list = ', '.join(map(str, nums))
        new_list = ', '.join(map(str, shifted))
        return json.dumps({'old_list': old_list, 'new_list': new_list})

    def get_task3_result_content(self, compute_data_str):
        compute_data = json.loads(compute_data_str)
        try:
            with open('task3_result.txt', 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if content.startswith('{') and '"' in content:
                result_data = json.load(f)
                html = result_data['html'].format(
                    old_list=compute_data['old_list'],
                    new_list=compute_data['new_list']
                )
                return json.dumps({
                    'css': result_data['css'],
                    'html': html,
                    'js': result_data['js']
                })
            else:
                css_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                css = css_match.group(1).strip() if css_match else ''
                js_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                js = js_match.group(1).strip() if js_match else ''
                body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                body_template = body_match.group(1).strip() if body_match else content
                body_template = re.sub(r'<style[^>]*>.*?</style>', '', body_template, flags=re.DOTALL)
                body_template = re.sub(r'<script[^>]*>.*?</script>', '', body_template, flags=re.DOTALL)
                html = body_template.format(
                    old_list=compute_data['old_list'],
                    new_list=compute_data['new_list']
                )
                return json.dumps({
                    'css': css,
                    'html': html,
                    'js': js
                })
        except Exception as e:
            return json.dumps({
                'css': '',
                'html': f"<h3 style='color:red'>Ошибка загрузки результата: {str(e)}</h3>",
                'js': ''
            })

    def get_task4_content(self):
        try:
            with open('task4.txt', 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if content.startswith('{') and '"' in content:
                data = json.loads(content)
                return json.dumps(data)
            else:
                css_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                css = css_match.group(1).strip() if css_match else ''
                js_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                js = js_match.group(1).strip() if js_match else ''
                app_match = re.search(r'<div id="app"[^>]*>(.*?)</div>', content, re.DOTALL)
                if app_match:
                    html = app_match.group(1).strip()
                else:
                    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                    body_html = body_match.group(1).strip() if body_match else content
                    body_html = re.sub(r'<style[^>]*>.*?</style>', '', body_html, flags=re.DOTALL)
                    body_html = re.sub(r'<script[^>]*>.*?</script>', '', body_html, flags=re.DOTALL)
                    html = body_html
                data = {
                    "css": css,
                    "html": html,
                    "js": js
                }
                return json.dumps(data)
        except Exception as e:
            return json.dumps({
                "css": "",
                "html": f"<h3 style='color:red'>Ошибка загрузки task4: {str(e)}</h3>",
                "js": ""
            })

    def compute_task4(self, data_str):
        data = json.loads(data_str)
        word = data['word']
        if not word:
            return json.dumps({'error': 'Нет слова для обработки.'})
        is_palindrome = word.lower() == word.lower()[::-1]
        message = 'Слово является палиндромом' if is_palindrome else 'Слово не является палиндромом'
        return json.dumps({'word': word, 'message': message})

    def get_task4_result_content(self, compute_data_str):
        compute_data = json.loads(compute_data_str)
        try:
            with open('task4_result.txt', 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if content.startswith('{') and '"' in content:
                result_data = json.load(f)
                html = result_data['html'].format(
                    word=compute_data['word'],
                    message=compute_data['message']
                )
                return json.dumps({
                    'css': result_data['css'],
                    'html': html,
                    'js': result_data['js']
                })
            else:
                css_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                css = css_match.group(1).strip() if css_match else ''
                js_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                js = js_match.group(1).strip() if js_match else ''
                body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                body_template = body_match.group(1).strip() if body_match else content
                body_template = re.sub(r'<style[^>]*>.*?</style>', '', body_template, flags=re.DOTALL)
                body_template = re.sub(r'<script[^>]*>.*?</script>', '', body_template, flags=re.DOTALL)
                html = body_template.format(
                    word=compute_data['word'],
                    message=compute_data['message']
                )
                return json.dumps({
                    'css': css,
                    'html': html,
                    'js': js
                })
        except Exception as e:
            return json.dumps({
                'css': '',
                'html': f"<h3 style='color:red'>Ошибка загрузки результата: {str(e)}</h3>",
                'js': ''
            })

    def get_task5_content(self):
        try:
            with open('task5.txt', 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if content.startswith('{') and '"' in content:
                data = json.loads(content)
                return json.dumps(data)
            else:
                css_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                css = css_match.group(1).strip() if css_match else ''
                js_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                js = js_match.group(1).strip() if js_match else ''
                app_match = re.search(r'<div id="app"[^>]*>(.*?)</div>', content, re.DOTALL)
                if app_match:
                    html = app_match.group(1).strip()
                else:
                    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                    body_html = body_match.group(1).strip() if body_match else content
                    body_html = re.sub(r'<style[^>]*>.*?</style>', '', body_html, flags=re.DOTALL)
                    body_html = re.sub(r'<script[^>]*>.*?</script>', '', body_html, flags=re.DOTALL)
                    html = body_html
                data = {
                    "css": css,
                    "html": html,
                    "js": js
                }
                return json.dumps(data)
        except Exception as e:
            return json.dumps({
                "css": "",
                "html": f"<h3 style='color:red'>Ошибка загрузки task5: {str(e)}</h3>",
                "js": ""
            })

    def compute_task5(self, data_str):
        data = json.loads(data_str)
        numbers = data['numbers']
        if not numbers:
            return json.dumps({'error': 'Нет данных для обработки.'})
        original = numbers[:]
        n = len(numbers)
        for i in range(n):
            for j in range(n - i - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        old_list = ', '.join(map(str, original))
        new_list = ', '.join(map(str, numbers))
        return json.dumps({'old_list': old_list, 'new_list': new_list})

    def get_task5_result_content(self, compute_data_str):
        compute_data = json.loads(compute_data_str)
        try:
            with open('task5_result.txt', 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if content.startswith('{') and '"' in content:
                result_data = json.load(f)
                html = result_data['html'].format(
                    old_list=compute_data['old_list'],
                    new_list=compute_data['new_list']
                )
                return json.dumps({
                    'css': result_data['css'],
                    'html': html,
                    'js': result_data['js']
                })
            else:
                css_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                css = css_match.group(1).strip() if css_match else ''
                js_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                js = js_match.group(1).strip() if js_match else ''
                body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                body_template = body_match.group(1).strip() if body_match else content
                body_template = re.sub(r'<style[^>]*>.*?</style>', '', body_template, flags=re.DOTALL)
                body_template = re.sub(r'<script[^>]*>.*?</script>', '', body_template, flags=re.DOTALL)
                html = body_template.format(
                    old_list=compute_data['old_list'],
                    new_list=compute_data['new_list']
                )
                return json.dumps({
                    'css': css,
                    'html': html,
                    'js': js
                })
        except Exception as e:
            return json.dumps({
                'css': '',
                'html': f"<h3 style='color:red'>Ошибка загрузки результата: {str(e)}</h3>",
                'js': ''
            })

    def get_task6_content(self):
        try:
            with open('task6.txt', 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if content.startswith('{') and '"' in content:
                data = json.loads(content)
                return json.dumps(data)
            else:
                css_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                css = css_match.group(1).strip() if css_match else ''
                js_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                js = js_match.group(1).strip() if js_match else ''
                app_match = re.search(r'<div id="app"[^>]*>(.*?)</div>', content, re.DOTALL)
                if app_match:
                    html = app_match.group(1).strip()
                else:
                    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                    body_html = body_match.group(1).strip() if body_match else content
                    body_html = re.sub(r'<style[^>]*>.*?</style>', '', body_html, flags=re.DOTALL)
                    body_html = re.sub(r'<script[^>]*>.*?</script>', '', body_html, flags=re.DOTALL)
                    html = body_html
                data = {
                    "css": css,
                    "html": html,
                    "js": js
                }
                return json.dumps(data)
        except Exception as e:
            return json.dumps({
                "css": "",
                "html": f"<h3 style='color:red'>Ошибка загрузки task6: {str(e)}</h3>",
                "js": ""
            })

    def compute_task6(self, data_str):
        data = json.loads(data_str)
        list1 = data['list1']
        list2 = data['list2']
        if not list1 or not list2:
            return json.dumps({'error': 'Нет данных для обработки.'})
        merged = sorted(set(list1 + list2))
        merged_list = ', '.join(map(str, merged))
        return json.dumps({'merged_list': merged_list})

    def get_task6_result_content(self, compute_data_str):
        compute_data = json.loads(compute_data_str)
        try:
            with open('task6_result.txt', 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if content.startswith('{') and '"' in content:
                result_data = json.load(f)
                html = result_data['html'].format(
                    merged_list=compute_data['merged_list']
                )
                return json.dumps({
                    'css': result_data['css'],
                    'html': html,
                    'js': result_data['js']
                })
            else:
                css_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                css = css_match.group(1).strip() if css_match else ''
                js_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                js = js_match.group(1).strip() if js_match else ''
                body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                body_template = body_match.group(1).strip() if body_match else content
                body_template = re.sub(r'<style[^>]*>.*?</style>', '', body_template, flags=re.DOTALL)
                body_template = re.sub(r'<script[^>]*>.*?</script>', '', body_template, flags=re.DOTALL)
                html = body_template.format(
                    merged_list=compute_data['merged_list']
                )
                return json.dumps({
                    'css': css,
                    'html': html,
                    'js': js
                })
        except Exception as e:
            return json.dumps({
                'css': '',
                'html': f"<h3 style='color:red'>Ошибка загрузки результата: {str(e)}</h3>",
                'js': ''
            })

    def get_task7_content(self):
        try:
            with open('task7.txt', 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if content.startswith('{') and '"' in content:
                data = json.loads(content)
                return json.dumps(data)
            else:
                css_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                css = css_match.group(1).strip() if css_match else ''
                js_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                js = js_match.group(1).strip() if js_match else ''
                app_match = re.search(r'<div id="app"[^>]*>(.*?)</div>', content, re.DOTALL)
                if app_match:
                    html = app_match.group(1).strip()
                else:
                    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                    body_html = body_match.group(1).strip() if body_match else content
                    body_html = re.sub(r'<style[^>]*>.*?</style>', '', body_html, flags=re.DOTALL)
                    body_html = re.sub(r'<script[^>]*>.*?</script>', '', body_html, flags=re.DOTALL)
                    html = body_html
                data = {
                    "css": css,
                    "html": html,
                    "js": js
                }
                return json.dumps(data)
        except Exception as e:
            return json.dumps({
                "css": "",
                "html": f"<h3 style='color:red'>Ошибка загрузки task7: {str(e)}</h3>",
                "js": ""
            })

    def compute_task7(self, data_str):
        data = json.loads(data_str)
        detail = data['detail'].lower()
        if not detail:
            return json.dumps({'error': 'Нет названия детали.'})
        shop = [
            ['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100],
            ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]
        ]
        count = sum(1 for d, _ in shop if d.lower() == detail)
        total = sum(p for d, p in shop if d.lower() == detail)
        return json.dumps({'detail': data['detail'], 'count': count, 'total': total})

    def get_task7_result_content(self, compute_data_str):
        compute_data = json.loads(compute_data_str)
        try:
            with open('task7_result.txt', 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if content.startswith('{') and '"' in content:
                result_data = json.load(f)
                html = result_data['html'].format(
                    detail=compute_data['detail'],
                    count=compute_data['count'],
                    total=compute_data['total']
                )
                return json.dumps({
                    'css': result_data['css'],
                    'html': html,
                    'js': result_data['js']
                })
            else:
                css_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                css = css_match.group(1).strip() if css_match else ''
                js_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                js = js_match.group(1).strip() if js_match else ''
                body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                body_template = body_match.group(1).strip() if body_match else content
                body_template = re.sub(r'<style[^>]*>.*?</style>', '', body_template, flags=re.DOTALL)
                body_template = re.sub(r'<script[^>]*>.*?</script>', '', body_template, flags=re.DOTALL)
                html = body_template.format(
                    detail=compute_data['detail'],
                    count=compute_data['count'],
                    total=compute_data['total']
                )
                return json.dumps({
                    'css': css,
                    'html': html,
                    'js': js
                })
        except Exception as e:
            return json.dumps({
                'css': '',
                'html': f"<h3 style='color:red'>Ошибка загрузки результата: {str(e)}</h3>",
                'js': ''
            })

    def get_task8_content(self):
        try:
            with open('task8.txt', 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if content.startswith('{') and '"' in content:
                data = json.loads(content)
                return json.dumps(data)
            else:
                css_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                css = css_match.group(1).strip() if css_match else ''
                js_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                js = js_match.group(1).strip() if js_match else ''
                app_match = re.search(r'<div id="app"[^>]*>(.*?)</div>', content, re.DOTALL)
                if app_match:
                    html = app_match.group(1).strip()
                else:
                    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                    body_html = body_match.group(1).strip() if body_match else content
                    body_html = re.sub(r'<style[^>]*>.*?</style>', '', body_html, flags=re.DOTALL)
                    body_html = re.sub(r'<script[^>]*>.*?</script>', '', body_html, flags=re.DOTALL)
                    html = body_html
                data = {
                    "css": css,
                    "html": html,
                    "js": js
                }
                return json.dumps(data)
        except Exception as e:
            return json.dumps({
                "css": "",
                "html": f"<h3 style='color:red'>Ошибка загрузки task8: {str(e)}</h3>",
                "js": ""
            })

    def compute_task8(self, data_str):
        data = json.loads(data_str)
        n = data['n']
        songs = data['songs']
        if n != len(songs):
            return json.dumps({'error': 'Количество песен не совпадает.'})
        violator_songs = {
            'World in My Eyes': 4.86,
            'Sweetest Perfection': 4.43,
            'Personal Jesus': 4.56,
            'Halo': 4.9,
            'Waiting for the Night': 6.07,
            'Enjoy the Silence': 4.20,
            'Policy of Truth': 4.76,
            'Blue Dress': 4.29,
            'Clean': 5.83
        }
        total_time = 0.0
        for song in songs:
            if song not in violator_songs:
                return json.dumps({'error': f'Песня "{song}" не найдена.'})
            total_time += violator_songs[song]
        total_time_str = f"{total_time:.2f}"
        return json.dumps({'total_time': f"Общее время звучания песен — {total_time_str} минуты"})

    def get_task8_result_content(self, compute_data_str):
        compute_data = json.loads(compute_data_str)
        try:
            with open('task8_result.txt', 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if content.startswith('{') and '"' in content:
                result_data = json.load(f)
                html = result_data['html'].format(
                    total_time=compute_data['total_time']
                )
                return json.dumps({
                    'css': result_data['css'],
                    'html': html,
                    'js': result_data['js']
                })
            else:
                css_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                css = css_match.group(1).strip() if css_match else ''
                js_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                js = js_match.group(1).strip() if js_match else ''
                body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                body_template = body_match.group(1).strip() if body_match else content
                body_template = re.sub(r'<style[^>]*>.*?</style>', '', body_template, flags=re.DOTALL)
                body_template = re.sub(r'<script[^>]*>.*?</script>', '', body_template, flags=re.DOTALL)
                html = body_template.format(
                    total_time=compute_data['total_time']
                )
                return json.dumps({
                    'css': css,
                    'html': html,
                    'js': js
                })
        except Exception as e:
            return json.dumps({
                'css': '',
                'html': f"<h3 style='color:red'>Ошибка загрузки результата: {str(e)}</h3>",
                'js': ''
            })

    def get_task9_content(self):
        try:
            with open('task9.txt', 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if content.startswith('{') and '"' in content:
                data = json.loads(content)
                return json.dumps(data)
            else:
                css_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                css = css_match.group(1).strip() if css_match else ''
                js_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                js = js_match.group(1).strip() if js_match else ''
                app_match = re.search(r'<div id="app"[^>]*>(.*?)</div>', content, re.DOTALL)
                if app_match:
                    html = app_match.group(1).strip()
                else:
                    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                    body_html = body_match.group(1).strip() if body_match else content
                    body_html = re.sub(r'<style[^>]*>.*?</style>', '', body_html, flags=re.DOTALL)
                    body_html = re.sub(r'<script[^>]*>.*?</script>', '', body_html, flags=re.DOTALL)
                    html = body_html
                data = {
                    "css": css,
                    "html": html,
                    "js": js
                }
                return json.dumps(data)
        except Exception as e:
            return json.dumps({
                "css": "",
                "html": f"<h3 style='color:red'>Ошибка загрузки task9: {str(e)}</h3>",
                "js": ""
            })

    def compute_task9(self, data_str):
        data = json.loads(data_str)
        skates = sorted(data['skates'])
        feet = sorted(data['feet'])
        if not skates or not feet:
            return json.dumps({'error': 'Нет данных для обработки.'})
        i = j = 0
        max_people = 0
        while i < len(skates) and j < len(feet):
            if skates[i] == feet[j]:
                max_people += 1
                i += 1
                j += 1
            elif skates[i] < feet[j]:
                i += 1
            else:
                j += 1
        return json.dumps({'max_people': max_people})

    def get_task9_result_content(self, compute_data_str):
        compute_data = json.loads(compute_data_str)
        try:
            with open('task9_result.txt', 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if content.startswith('{') and '"' in content:
                result_data = json.load(f)
                html = result_data['html'].format(
                    max_people=compute_data['max_people']
                )
                return json.dumps({
                    'css': result_data['css'],
                    'html': html,
                    'js': result_data['js']
                })
            else:
                css_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                css = css_match.group(1).strip() if css_match else ''
                js_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                js = js_match.group(1).strip() if js_match else ''
                body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                body_template = body_match.group(1).strip() if body_match else content
                body_template = re.sub(r'<style[^>]*>.*?</style>', '', body_template, flags=re.DOTALL)
                body_template = re.sub(r'<script[^>]*>.*?</script>', '', body_template, flags=re.DOTALL)
                html = body_template.format(
                    max_people=compute_data['max_people']
                )
                return json.dumps({
                    'css': css,
                    'html': html,
                    'js': js
                })
        except Exception as e:
            return json.dumps({
                'css': '',
                'html': f"<h3 style='color:red'>Ошибка загрузки результата: {str(e)}</h3>",
                'js': ''
            })

    def get_task10_content(self):
        try:
            with open('task10.txt', 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if content.startswith('{') and '"' in content:
                data = json.loads(content)
                return json.dumps(data)
            else:
                css_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                css = css_match.group(1).strip() if css_match else ''
                js_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                js = js_match.group(1).strip() if js_match else ''
                app_match = re.search(r'<div id="app"[^>]*>(.*?)</div>', content, re.DOTALL)
                if app_match:
                    html = app_match.group(1).strip()
                else:
                    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                    body_html = body_match.group(1).strip() if body_match else content
                    body_html = re.sub(r'<style[^>]*>.*?</style>', '', body_html, flags=re.DOTALL)
                    body_html = re.sub(r'<script[^>]*>.*?</script>', '', body_html, flags=re.DOTALL)
                    html = body_html
                data = {
                    "css": css,
                    "html": html,
                    "js": js
                }
                return json.dumps(data)
        except Exception as e:
            return json.dumps({
                "css": "",
                "html": f"<h3 style='color:red'>Ошибка загрузки task10: {str(e)}</h3>",
                "js": ""
            })

    def compute_task10(self, data_str):
        data = json.loads(data_str)
        n = data['n']
        k = data['k']
        if n < 1 or k < 1:
            return json.dumps({'error': 'N и K должны быть >=1.'})
        people = list(range(1, n + 1))
        index = 0
        lines = [
            f"Количество человек: {n}",
            f"Какое число в считалке? {k}",
            f"Значит, выбывает каждый {k}-й человек",
            f"Текущий круг людей: {people}",
            f"Начало счёта с номера 1"
        ]
        while len(people) > 1:
            index = (index + k - 1) % len(people)
            out = people.pop(index)
            lines.append(f"Выбывает человек под номером {out}")
            lines.append(f"Текущий круг людей: {people}")
            if len(people) > 1:
                next_start = people[index % len(people)] if index < len(people) else people[0]
                lines.append(f"Начало счёта с номера {next_start}")
        lines.append(f"Остался человек под номером {people[0]}")
        simulation = '\n'.join(lines)
        return json.dumps({'simulation': simulation})

    def get_task10_result_content(self, compute_data_str):
        compute_data = json.loads(compute_data_str)
        try:
            with open('task10_result.txt', 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if content.startswith('{') and '"' in content:
                result_data = json.load(f)
                html = result_data['html'].format(
                    simulation=compute_data['simulation']
                )
                return json.dumps({
                    'css': result_data['css'],
                    'html': html,
                    'js': result_data['js']
                })
            else:
                css_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                css = css_match.group(1).strip() if css_match else ''
                js_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                js = js_match.group(1).strip() if js_match else ''
                body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                body_template = body_match.group(1).strip() if body_match else content
                body_template = re.sub(r'<style[^>]*>.*?</style>', '', body_template, flags=re.DOTALL)
                body_template = re.sub(r'<script[^>]*>.*?</script>', '', body_template, flags=re.DOTALL)
                html = body_template.format(
                    simulation=compute_data['simulation']
                )
                return json.dumps({
                    'css': css,
                    'html': html,
                    'js': js
                })
        except Exception as e:
            return json.dumps({
                'css': '',
                'html': f"<h3 style='color:red'>Ошибка загрузки результата: {str(e)}</h3>",
                'js': ''
            })

    def get_task11_content(self):
        try:
            with open('task11.txt', 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if content.startswith('{') and '"' in content:
                data = json.loads(content)
                return json.dumps(data)
            else:
                css_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                css = css_match.group(1).strip() if css_match else ''
                js_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                js = js_match.group(1).strip() if js_match else ''
                app_match = re.search(r'<div id="app"[^>]*>(.*?)</div>', content, re.DOTALL)
                if app_match:
                    html = app_match.group(1).strip()
                else:
                    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                    body_html = body_match.group(1).strip() if body_match else content
                    body_html = re.sub(r'<style[^>]*>.*?</style>', '', body_html, flags=re.DOTALL)
                    body_html = re.sub(r'<script[^>]*>.*?</script>', '', body_html, flags=re.DOTALL)
                    html = body_html
                data = {
                    "css": css,
                    "html": html,
                    "js": js
                }
                return json.dumps(data)
        except Exception as e:
            return json.dumps({
                "css": "",
                "html": f"<h3 style='color:red'>Ошибка загрузки task11: {str(e)}</h3>",
                "js": ""
            })

    def compute_task11(self, data_str):
        data = json.loads(data_str)
        sequence = data['sequence']
        if not sequence:
            return json.dumps({'error': 'Нет данных для обработки.'})
        n = len(sequence)
        min_append = n
        append_seq = []
        for i in range(n + 1):
            candidate = sequence + sequence[:i][::-1]
            if candidate == candidate[::-1]:
                if i < min_append:
                    min_append = i
                    append_seq = sequence[:i][::-1]
        count = min_append
        append_list = ', '.join(map(str, append_seq)) if append_seq else ''
        seq_list = ', '.join(map(str, sequence))
        return json.dumps({
            'sequence': seq_list,
            'count': count,
            'append_list': append_list
        })

    def get_task11_result_content(self, compute_data_str):
        compute_data = json.loads(compute_data_str)
        try:
            with open('task11_result.txt', 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if content.startswith('{') and '"' in content:
                result_data = json.load(f)
                html = result_data['html'].format(
                    sequence=compute_data['sequence'],
                    count=compute_data['count'],
                    append_list=compute_data['append_list']
                )
                return json.dumps({
                    'css': result_data['css'],
                    'html': html,
                    'js': result_data['js']
                })
            else:
                css_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                css = css_match.group(1).strip() if css_match else ''
                js_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                js = js_match.group(1).strip() if js_match else ''
                body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
                body_template = body_match.group(1).strip() if body_match else content
                body_template = re.sub(r'<style[^>]*>.*?</style>', '', body_template, flags=re.DOTALL)
                body_template = re.sub(r'<script[^>]*>.*?</script>', '', body_template, flags=re.DOTALL)
                html = body_template.format(
                    sequence=compute_data['sequence'],
                    count=compute_data['count'],
                    append_list=compute_data['append_list']
                )
                return json.dumps({
                    'css': css,
                    'html': html,
                    'js': js
                })
        except Exception as e:
            return json.dumps({
                'css': '',
                'html': f"<h3 style='color:red'>Ошибка загрузки результата: {str(e)}</h3>",
                'js': ''
            })

    def backToMain(self):
        try:
            with open('main.txt', 'r', encoding='utf-8') as f:
                content = f.read().strip()
            if content.startswith('{') and '"' in content:
                data = json.loads(content)
            else:
                css_match = re.search(r'<style[^>]*>(.*?)</style>', content, re.DOTALL)
                css = css_match.group(1).strip() if css_match else ''
                js_match = re.search(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                js = js_match.group(1).strip() if js_match else ''
                app_match = re.search(r'<div id="app"[^>]*>(.*?)</div>', content, re.DOTALL)
                if app_match:
                    html = app_match.group(1).strip()
                else:
                    html = content
                data = {
                    "css": css,
                    "html": html,
                    "js": js
                }
            return json.dumps(data)
        except Exception as e:
            return json.dumps({
                "css": "",
                "html": f"<h3 style='color:red'>Ошибка: {str(e)}</h3>",
                "js": ""
            })

    def exit_app(self):
        webview.windows[0].destroy()

with open('main.txt', 'r', encoding='utf-8') as f:
    html_content = f.read()

html_file = os.path.join(os.path.dirname(__file__), 'index.html')
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

html_url = f"file://{os.path.abspath(html_file)}"

api = Api()
webview.create_window("Задания", url=html_url, js_api=api, fullscreen=True)
webview.start()
'''

task1_txt = r'''
<html>
  <head>
    <style>
      .task-container {
        max-width: 600px;
        max-height: 80vh;
        overflow-y: auto;
        padding: 40px;
        border-radius: 25px;
        border: 2px solid #fff;
        background: rgba(0, 0, 0, .6);
        box-shadow: 0 0 25px rgba(255, 255, 255, .4);
        color: #fff;
        font-family: Arial, sans-serif;
      }
      .task-container::-webkit-scrollbar {
        width: 8px;
      }
      .task-container::-webkit-scrollbar-track {
        background: rgba(0, 0, 0, .3);
        border-top-right-radius: 25px;
        border-bottom-right-radius: 25px;
      }
      .task-container::-webkit-scrollbar-thumb {
        background: rgb(61, 106, 255);
        border-radius: 25px;
        margin: 4px 0;
      }
      .task-container::-webkit-scrollbar-thumb:hover {
        background: rgb(0, 142, 236);
      }
      .task-h2 {
        text-align: center;
        color: rgb(61, 106, 255);
        text-transform: uppercase;
        letter-spacing: 1px;
      }
      .task-label {
        font-weight: 600;
        color: #fff;
      }
      .task-input {
        padding: 10px;
        border-radius: 8px;
        border: 1px solid rgb(61, 106, 255);
        background: rgba(255, 255, 255, .1);
        color: #fff;
        margin: 5px;
        width: 200px;
      }
      .task-input::placeholder {
        color: rgba(255, 255, 255, .7);
      }
      .task-button {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(61, 106, 255);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: #fff;
        overflow: hidden;
        transition: all .2s ease-in;
        cursor: pointer;
        margin: 10px;
      }
      .task-button:hover {
        background: rgb(61, 106, 255);
        box-shadow: 0 0 20px 3px rgba(0, 142, 236, .815);
        transition: all .2s ease-out;
      }
      .back-section {
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, .3);
        text-align: center;
      }
      .error-modal {
        display: none;
        position: fixed;
        z-index: 1000;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, .8);
        backdrop-filter: blur(5px);
        opacity: 0;
        transition: opacity .3s ease;
      }
      .error-content {
        background: linear-gradient(135deg, rgba(0, 0, 0, .95), rgba(20, 20, 40, .95));
        border: 2px solid rgb(255, 61, 61);
        border-radius: 15px;
        margin: 15% auto;
        padding: 30px;
        width: 80%;
        max-width: 400px;
        color: #fff;
        text-align: center;
        box-shadow: 0 0 40px rgba(255, 61, 61, .3), inset 0 0 20px rgba(255, 255, 255, .05);
        animation: errorSlideIn .3s ease-out;
      }
      @keyframes errorSlideIn {
        from {
          transform: translateY(-50px);
          opacity: 0;
        }
        to {
          transform: translateY(0);
          opacity: 1;
        }
      }
      .error-content h3 {
        color: rgb(255, 61, 61);
        margin-bottom: 15px;
        font-size: 24px;
        text-transform: uppercase;
        letter-spacing: 1px;
      }
      .error-content p {
        font-size: 16px;
        margin-bottom: 20px;
        line-height: 1.4;
      }
      .error-close {
        color: rgba(255, 255, 255, .7);
        float: right;
        font-size: 28px;
        font-weight: 700;
        cursor: pointer;
        transition: color .2s ease;
        background: none;
        border: none;
        line-height: 1;
      }
      .error-close:hover {
        color: rgb(255, 61, 61);
      }
      .error-ok {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(255, 61, 61);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: #fff;
        cursor: pointer;
        margin-top: 10px;
        transition: all .2s ease;
      }
      .error-ok:hover {
        background: rgb(255, 61, 61);
        box-shadow: 0 0 20px 3px rgba(255, 0, 0, .5);
      }
    </style>
  </head>
  <body>
    <h2 class="task-h2">Задание 1. Видеокарты</h2>
    <label class="task-label">Количество видеокарт:</label>
    <input type="number" id="n" min="1" class="task-input" placeholder="Введите число"><br><br>
    <button class="task-button" id="genBtn">Генерировать поля</button><br><br>
    <div id="fields"></div><br>
    <button class="task-button" id="computeBtn" style="display:none;">Вычислить</button>
    <div class="back-section">
      <button class="task-button" id="toMenuBtn">Назад к меню</button>
    </div>
    <script>
      (function(){
        window.originalTaskHTML = document.querySelector('.task-container') ? document.querySelector('.task-container').innerHTML : document.getElementById('app').innerHTML || '';
        if (!document.getElementById('task1-style')) {
          const s = document.createElement('style');
          s.id = 'task1-style';
          s.textContent = window.__task_css__ || '';
          document.head.appendChild(s);
        }
        window.closeModal = function(modal) {
          modal.style.opacity = '0';
          setTimeout(() => { modal.remove(); }, 300);
        };
        window.showError = function(message) {
          const modal = document.createElement('div');
          modal.className = 'error-modal';
          modal.innerHTML = `<div class="error-content"><button class="error-close" aria-label="close">&times;</button><h3>Ошибка!</h3><p>${message}</p><button class="error-ok">OK</button></div>`;
          document.body.appendChild(modal);
          modal.style.display = 'block';
          setTimeout(() => { modal.style.opacity = '1'; }, 10);
          const closeSpan = modal.querySelector('.error-close');
          closeSpan.onclick = () => closeModal(modal);
          modal.querySelector('.error-ok').onclick = () => closeModal(modal);
          modal.addEventListener('click', (e) => {
            if (e.target === modal) closeModal(modal);
          });
        };
        window.generateFields = function() {
          const nInput = document.getElementById('n');
          let n = parseInt(nInput.value);
          if (n < 1 || isNaN(n)) {
            window.showError('Введите корректное число видеокарт (минимум 1)');
            return;
          }
          let fields = '';
          for (let i = 1; i <= n; i++) {
            fields += `<label class="task-label">Видеокарта ${i}: </label><input type="number" id="card${i}" min="0" class="task-input" placeholder="Введите номер модели"><br><br>`;
          }
          document.getElementById('fields').innerHTML = fields;
          document.getElementById('computeBtn').style.display = 'block';
          const container = document.querySelector('.task-container') || document.getElementById('app');
          if (container) container.scrollTop = 0;
        };
        window.compute = async function() {
          let n = parseInt(document.getElementById('n').value);
          let cards = [];
          let valid = true;
          for (let i = 1; i <= n; i++) {
            let val = parseInt(document.getElementById(`card${i}`).value);
            if (isNaN(val) || val < 0) {
              window.showError(`Введите корректное значение для видеокарты ${i}`);
              valid = false;
              break;
            }
            cards.push(val);
          }
          if (!valid) return;
          let data = { n: n, cards: cards };
          const compute_result_str = await pywebview.api.compute_task1(JSON.stringify(data));
          const compute_data = JSON.parse(compute_result_str);
          if (compute_data.error) {
            window.showError(compute_data.error);
            return;
          }
          const styleText = document.getElementById('task1-style') ? document.getElementById('task1-style').textContent : '';
          const scriptText = window.__task_js__ || '';
          const htmlText = window.originalTaskHTML || (document.querySelector('.task-container') ? document.querySelector('.task-container').innerHTML : document.getElementById('app').innerHTML);
          window.task1Data = { css: styleText, html: htmlText, js: scriptText };
          const app = document.getElementById('app');
          app.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
          app.style.opacity = '0';
          app.style.transform = 'translateY(-30px)';
          setTimeout(async () => {
            const result_response = await pywebview.api.get_task1_result_content(JSON.stringify(compute_data));
            const result_data = JSON.parse(result_response);
            let style = document.getElementById('result-style');
            if (style) style.remove();
            style = document.createElement('style');
            style.id = 'result-style';
            style.textContent = result_data.css;
            document.head.appendChild(style);
            app.className = 'result-wrapper';
            app.replaceChildren();
            app.innerHTML = result_data.html;
            let script = document.getElementById('result-script');
            if (script) script.remove();
            script = document.createElement('script');
            script.id = 'result-script';
            script.textContent = result_data.js;
            document.body.appendChild(script);
            app.style.transform = 'translateY(30px)';
            app.offsetHeight;
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '1';
            app.style.transform = 'translateY(0)';
          }, 400);
        };
        window.backToMenu = async function() {
          try {
            const responseStr = await pywebview.api.backToMain();
            const data = JSON.parse(responseStr);
            const app = document.getElementById('app') || document.body;
            const oldStyle = document.getElementById('result-style') || document.getElementById('main-style');
            if (oldStyle) oldStyle.remove();
            const oldScript = document.getElementById('result-script') || document.getElementById('main-script');
            if (oldScript) oldScript.remove();
            if (data.css) {
              const style = document.createElement('style');
              style.id = 'main-style';
              style.textContent = data.css;
              document.head.appendChild(style);
            }
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '0';
            app.style.transform = 'translateY(20px)';
            setTimeout(() => {
              app.replaceChildren();
              app.innerHTML = data.html || '';
              app.className = 'container';
              if (data.js) {
                const script = document.createElement('script');
                script.id = 'main-script';
                script.textContent = data.js;
                document.body.appendChild(script);
              }
              app.style.transform = 'translateY(-20px)';
              app.offsetHeight;
              app.style.opacity = '1';
              app.style.transform = 'translateY(0)';
              if (typeof attachHandlers === 'function') setTimeout(attachHandlers, 50);
            }, 500);
          } catch (e) {
            window.showError('Ошибка при возврате в меню: ' + (e && e.message ? e.message : String(e)));
          }
        };
        window.__task_js__ = (function(){ return `/* task js source placeholder */`; })();
        function attachHandlers(){
          const gen = document.getElementById('genBtn');
          if (gen) gen.addEventListener('click', window.generateFields);
          const comp = document.getElementById('computeBtn');
          if (comp) comp.addEventListener('click', window.compute);
          const menu = document.getElementById('toMenuBtn');
          if (menu) menu.addEventListener('click', window.backToMenu);
          const task1 = document.getElementById('task1Btn');
          if (task1 && !task1.dataset.bound) {
            task1.dataset.bound = 'true';
            task1.addEventListener('click', async () => {
              const resp = await pywebview.api.load_task1();
              const d = JSON.parse(resp);
              const app = document.getElementById('app');
              app.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
              app.style.opacity = '0';
              app.style.transform = 'translateY(30px)';
              setTimeout(() => {
                app.replaceChildren();
                app.innerHTML = d.html;
                if (d.css) {
                  const s = document.createElement('style');
                  s.id = 'task1-style';
                  s.textContent = d.css;
                  document.head.appendChild(s);
                }
                if (d.js) {
                  const sc = document.createElement('script');
                  sc.id = 'task1-script';
                  sc.textContent = d.js;
                  document.body.appendChild(sc);
                }
                app.style.transform = 'translateY(-20px)';
                app.offsetHeight;
                app.style.opacity = '1';
                app.style.transform = 'translateY(0)';
              }, 400);
            });
          }
        }
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', attachHandlers);
        } else {
          attachHandlers();
        }
      })();
    </script>
  </body>
</html>
'''

task1_result_txt = r'''
<html>
  <head>
    <style>
      .result-main-container {
        max-width: 800px;
        padding: 40px;
        border-radius: 25px;
        border: 2px solid white;
        background: rgba(0, 0, 0, 0.6);
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.4);
        color: white;
        font-family: Arial, sans-serif;
        margin: 0 auto;
      }
      .result-container {
        text-align: center;
        padding: 20px;
      }
      .result-h2 {
        color: rgb(61, 106, 255);
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 30px;
      }
      .lists {
        display: flex;
        justify-content: space-around;
        gap: 20px;
        margin: 20px 0;
      }
      .list-box {
        flex: 1;
        max-width: 45%;
        border: 2px solid yellow;
        border-radius: 10px;
        padding: 15px;
        background: rgba(255, 255, 0, 0.1);
      }
      .list-box h3 {
        color: rgb(61, 106, 255);
        margin-bottom: 10px;
        font-size: 16px;
        text-transform: uppercase;
      }
      .list-box pre {
        color: white;
        background: none;
        margin: 0;
        font-family: monospace;
        white-space: pre-wrap;
        font-size: 14px;
      }
      .back-section {
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, 0.3);
        text-align: center;
      }
      .back-btn {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(61, 106, 255);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: rgb(61, 106, 255);
        cursor: pointer;
        margin: 10px;
        transition: all 0.2s ease;
      }
      .back-btn:hover {
        background: rgb(61, 106, 255);
        color: white;
        box-shadow: 0 0 20px rgba(0, 142, 236, 0.5);
      }
      .result-wrapper {
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
      }
      body {
        overflow: hidden;
        margin: 0;
      }
    </style>
  </head>
  <body>
    <div class="result-main-container">
      <div class="result-container">
        <h2 class="result-h2">Результат</h2>
        <div class="lists">
          <div class="list-box">
            <h3>Старый список видеокарт:</h3>
            <pre>[ {old_list} ]</pre>
          </div>
          <div class="list-box">
            <h3>Новый список видеокарт:</h3>
            <pre>[ {new_list} ]</pre>
          </div>
        </div>
        <div class="back-section">
          <button class="back-btn" id="backToInputBtn">Назад</button>
          <button class="back-btn" id="toMenuBtn">В меню</button>
        </div>
      </div>
    </div>
    <script>
      (function(){
        window.backToInput = function() {
          const app = document.getElementById('app');
          app.style.transition = 'all 0.5s ease';
          app.style.opacity = '0';
          app.style.transform = 'translateY(-100%)';
          setTimeout(() => {
            const resultStyle = document.getElementById('result-style');
            if (resultStyle) resultStyle.remove();
            const resultScript = document.getElementById('result-script');
            if (resultScript) resultScript.remove();
            const taskData = window.task1Data;
            if (!taskData) {
              alert('Ошибка: исходное задание не найдено');
              return;
            }
            const taskStyle = document.createElement('style');
            taskStyle.id = 'task1-style';
            taskStyle.textContent = taskData.css || '';
            document.head.appendChild(taskStyle);
            app.className = 'task-container';
            app.innerHTML = taskData.html || '';
            const taskScript = document.createElement('script');
            taskScript.id = 'task1-script';
            taskScript.textContent = taskData.js || '';
            document.body.appendChild(taskScript);
            setTimeout(() => {
              const gen = document.getElementById('genBtn');
              if (gen && window.generateFields) gen.addEventListener('click', window.generateFields);
              const comp = document.getElementById('computeBtn');
              if (comp && window.compute) comp.addEventListener('click', window.compute);
              const menu = document.getElementById('toMenuBtn');
              if (menu && window.backToMenu) menu.addEventListener('click', window.backToMenu);
              const n = document.getElementById('n');
              if (n) n.focus();
            }, 100);
            app.style.opacity = '1';
            app.style.transform = 'translateY(0)';
            app.style.transition = '';
          }, 500);
        };
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', function(){
            const b = document.getElementById('backToInputBtn');
            if (b) b.addEventListener('click', window.backToInput);
            const m = document.getElementById('toMenuBtn');
            if (m) m.addEventListener('click', window.backToMenu);
          });
        } else {
          const b = document.getElementById('backToInputBtn');
          if (b) b.addEventListener('click', window.backToInput);
          const m = document.getElementById('toMenuBtn');
          if (m) m.addEventListener('click', window.backToMenu);
        }
        window.backToMenu = async function() {
          try {
            const responseStr = await pywebview.api.backToMain();
            const data = JSON.parse(responseStr);
            const app = document.getElementById('app') || document.body;
            const oldStyle = document.getElementById('result-style') || document.getElementById('main-style');
            if (oldStyle) oldStyle.remove();
            const oldScript = document.getElementById('result-script') || document.getElementById('main-script');
            if (oldScript) oldScript.remove();
            if (data.css) {
              const style = document.createElement('style');
              style.id = 'main-style';
              style.textContent = data.css;
              document.head.appendChild(style);
            }
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '0';
            app.style.transform = 'translateY(20px)';
            setTimeout(() => {
              app.replaceChildren();
              app.innerHTML = data.html || '';
              app.className = 'container';
              if (data.js) {
                const script = document.createElement('script');
                script.id = 'main-script';
                script.textContent = data.js;
                document.body.appendChild(script);
              }
              app.style.transform = 'translateY(-20px)';
              app.offsetHeight;
              app.style.opacity = '1';
              app.style.transform = 'translateY(0)';
              if (typeof attachHandlers === 'function') setTimeout(attachHandlers, 50);
            }, 500);
          } catch (e) {
            window.showError('Ошибка при возврате в меню: ' + (e && e.message ? e.message : String(e)));
          }
        };
      })();
    </script>
  </body>
</html>
'''

task2_txt = r'''
<html>
  <head>
    <style>
      .task-container {
        max-width: 600px;
        max-height: 80vh;
        overflow-y: auto;
        padding: 40px;
        border-radius: 25px;
        border: 2px solid #fff;
        background: rgba(0, 0, 0, .6);
        box-shadow: 0 0 25px rgba(255, 255, 255, .4);
        color: #fff;
        font-family: Arial, sans-serif;
      }
      .task-container::-webkit-scrollbar {
        width: 8px;
      }
      .task-container::-webkit-scrollbar-track {
        background: rgba(0, 0, 0, .3);
        border-top-right-radius: 25px;
        border-bottom-right-radius: 25px;
      }
      .task-container::-webkit-scrollbar-thumb {
        background: rgb(61, 106, 255);
        border-radius: 25px;
        margin: 4px 0;
      }
      .task-container::-webkit-scrollbar-thumb:hover {
        background: rgb(0, 142, 236);
      }
      .task-h2 {
        text-align: center;
        color: rgb(61, 106, 255);
        text-transform: uppercase;
        letter-spacing: 1px;
      }
      .task-label {
        font-weight: 600;
        color: #fff;
      }
      .task-input {
        padding: 10px;
        border-radius: 8px;
        border: 1px solid rgb(61, 106, 255);
        background: rgba(255, 255, 255, .1);
        color: #fff;
        margin: 5px;
        width: 200px;
      }
      .task-input::placeholder {
        color: rgba(255, 255, 255, .7);
      }
      .task-button {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(61, 106, 255);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: #fff;
        overflow: hidden;
        transition: all .2s ease-in;
        cursor: pointer;
        margin: 10px;
      }
      .task-button:hover {
        background: rgb(61, 106, 255);
        box-shadow: 0 0 20px 3px rgba(0, 142, 236, .815);
        transition: all .2s ease-out;
      }
      .back-section {
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, .3);
        text-align: center;
      }
      .error-modal {
        display: none;
        position: fixed;
        z-index: 1000;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, .8);
        backdrop-filter: blur(5px);
        opacity: 0;
        transition: opacity .3s ease;
      }
      .error-content {
        background: linear-gradient(135deg, rgba(0, 0, 0, .95), rgba(20, 20, 40, .95));
        border: 2px solid rgb(255, 61, 61);
        border-radius: 15px;
        margin: 15% auto;
        padding: 30px;
        width: 80%;
        max-width: 400px;
        color: #fff;
        text-align: center;
        box-shadow: 0 0 40px rgba(255, 61, 61, .3), inset 0 0 20px rgba(255, 255, 255, .05);
        animation: errorSlideIn .3s ease-out;
      }
      @keyframes errorSlideIn {
        from {
          transform: translateY(-50px);
          opacity: 0;
        }
        to {
          transform: translateY(0);
          opacity: 1;
        }
      }
      .error-content h3 {
        color: rgb(255, 61, 61);
        margin-bottom: 15px;
        font-size: 24px;
        text-transform: uppercase;
        letter-spacing: 1px;
      }
      .error-content p {
        font-size: 16px;
        margin-bottom: 20px;
        line-height: 1.4;
      }
      .error-close {
        color: rgba(255, 255, 255, .7);
        float: right;
        font-size: 28px;
        font-weight: 700;
        cursor: pointer;
        transition: color .2s ease;
        background: none;
        border: none;
        line-height: 1;
      }
      .error-close:hover {
        color: rgb(255, 61, 61);
      }
      .error-ok {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(255, 61, 61);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: #fff;
        cursor: pointer;
        margin-top: 10px;
        transition: all .2s ease;
      }
      .error-ok:hover {
        background: rgb(255, 61, 61);
        box-shadow: 0 0 20px 3px rgba(255, 0, 0, .5);
      }
    </style>
  </head>
  <body>
    <h2 class="task-h2">Задание 2. Кино</h2>
    <label class="task-label">Количество фильмов:</label>
    <input type="number" id="n" min="1" class="task-input" placeholder="Введите число"><br><br>
    <button class="task-button" id="genBtn">Генерировать поля</button><br><br>
    <div id="fields"></div><br>
    <button class="task-button" id="computeBtn" style="display:none;">Вычислить</button>
    <div class="back-section">
      <button class="task-button" id="toMenuBtn">Назад к меню</button>
    </div>
    <script>
      (function(){
        window.originalTaskHTML = document.querySelector('.task-container') ? document.querySelector('.task-container').innerHTML : document.getElementById('app').innerHTML || '';
        if (!document.getElementById('task2-style')) {
          const s = document.createElement('style');
          s.id = 'task2-style';
          s.textContent = window.__task_css__ || '';
          document.head.appendChild(s);
        }
        window.closeModal = function(modal) {
          modal.style.opacity = '0';
          setTimeout(() => { modal.remove(); }, 300);
        };
        window.showError = function(message) {
          const modal = document.createElement('div');
          modal.className = 'error-modal';
          modal.innerHTML = `<div class="error-content"><button class="error-close" aria-label="close">&times;</button><h3>Ошибка!</h3><p>${message}</p><button class="error-ok">OK</button></div>`;
          document.body.appendChild(modal);
          modal.style.display = 'block';
          setTimeout(() => { modal.style.opacity = '1'; }, 10);
          const closeSpan = modal.querySelector('.error-close');
          closeSpan.onclick = () => closeModal(modal);
          modal.querySelector('.error-ok').onclick = () => closeModal(modal);
          modal.addEventListener('click', (e) => {
            if (e.target === modal) closeModal(modal);
          });
        };
        window.generateFields = function() {
          const nInput = document.getElementById('n');
          let n = parseInt(nInput.value);
          if (n < 1 || isNaN(n)) {
            window.showError('Введите корректное число фильмов (минимум 1)');
            return;
          }
          let fields = '';
          for (let i = 1; i <= n; i++) {
            fields += `<label class="task-label">Фильм ${i}: </label><input type="text" id="film${i}" class="task-input" placeholder="Введите название фильма"><br><br>`;
          }
          document.getElementById('fields').innerHTML = fields;
          document.getElementById('computeBtn').style.display = 'block';
          const container = document.querySelector('.task-container') || document.getElementById('app');
          if (container) container.scrollTop = 0;
        };
        window.compute = async function() {
          let n = parseInt(document.getElementById('n').value);
          let films = [];
          let valid = true;
          for (let i = 1; i <= n; i++) {
            let val = document.getElementById(`film${i}`).value.trim();
            if (!val) {
              window.showError(`Введите название для фильма ${i}`);
              valid = false;
              break;
            }
            films.push(val);
          }
          if (!valid) return;
          let data = { n: n, films: films };
          const compute_result_str = await pywebview.api.compute_task2(JSON.stringify(data));
          const compute_data = JSON.parse(compute_result_str);
          if (compute_data.error) {
            window.showError(compute_data.error);
            return;
          }
          const styleText = document.getElementById('task2-style') ? document.getElementById('task2-style').textContent : '';
          const scriptText = window.__task_js__ || '';
          const htmlText = window.originalTaskHTML || (document.querySelector('.task-container') ? document.querySelector('.task-container').innerHTML : document.getElementById('app').innerHTML);
          window.task2Data = { css: styleText, html: htmlText, js: scriptText };
          const app = document.getElementById('app');
          app.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
          app.style.opacity = '0';
          app.style.transform = 'translateY(-30px)';
          setTimeout(async () => {
            const result_response = await pywebview.api.get_task2_result_content(JSON.stringify(compute_data));
            const result_data = JSON.parse(result_response);
            let style = document.getElementById('result-style');
            if (style) style.remove();
            style = document.createElement('style');
            style.id = 'result-style';
            style.textContent = result_data.css;
            document.head.appendChild(style);
            app.className = 'result-wrapper';
            app.replaceChildren();
            app.innerHTML = result_data.html;
            let script = document.getElementById('result-script');
            if (script) script.remove();
            script = document.createElement('script');
            script.id = 'result-script';
            script.textContent = result_data.js;
            document.body.appendChild(script);
            app.style.transform = 'translateY(30px)';
            app.offsetHeight;
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '1';
            app.style.transform = 'translateY(0)';
          }, 400);
        };
        window.backToMenu = async function() {
          try {
            const responseStr = await pywebview.api.backToMain();
            const data = JSON.parse(responseStr);
            const app = document.getElementById('app') || document.body;
            const oldStyle = document.getElementById('result-style') || document.getElementById('main-style');
            if (oldStyle) oldStyle.remove();
            const oldScript = document.getElementById('result-script') || document.getElementById('main-script');
            if (oldScript) oldScript.remove();
            if (data.css) {
              const style = document.createElement('style');
              style.id = 'main-style';
              style.textContent = data.css;
              document.head.appendChild(style);
            }
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '0';
            app.style.transform = 'translateY(20px)';
            setTimeout(() => {
              app.replaceChildren();
              app.innerHTML = data.html || '';
              app.className = 'container';
              if (data.js) {
                const script = document.createElement('script');
                script.id = 'main-script';
                script.textContent = data.js;
                document.body.appendChild(script);
              }
              app.style.transform = 'translateY(-20px)';
              app.offsetHeight;
              app.style.opacity = '1';
              app.style.transform = 'translateY(0)';
              if (typeof attachHandlers === 'function') setTimeout(attachHandlers, 50);
            }, 500);
          } catch (e) {
            window.showError('Ошибка при возврате в меню: ' + (e && e.message ? e.message : String(e)));
          }
        };
        window.__task_js__ = (function(){ return `/* task js source placeholder */`; })();
        function attachHandlers(){
          const gen = document.getElementById('genBtn');
          if (gen) gen.addEventListener('click', window.generateFields);
          const comp = document.getElementById('computeBtn');
          if (comp) comp.addEventListener('click', window.compute);
          const menu = document.getElementById('toMenuBtn');
          if (menu) menu.addEventListener('click', window.backToMenu);
        }
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', attachHandlers);
        } else {
          attachHandlers();
        }
      })();
    </script>
  </body>
</html>
'''

task2_result_txt = r'''
<html>
  <head>
    <style>
      .result-main-container {
        max-width: 800px;
        padding: 40px;
        border-radius: 25px;
        border: 2px solid white;
        background: rgba(0, 0, 0, 0.6);
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.4);
        color: white;
        font-family: Arial, sans-serif;
        margin: 0 auto;
      }
      .result-container {
        text-align: center;
        padding: 20px;
      }
      .result-h2 {
        color: rgb(61, 106, 255);
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 30px;
      }
      .lists {
        display: flex;
        justify-content: space-around;
        gap: 20px;
        margin: 20px 0;
      }
      .list-box {
        flex: 1;
        max-width: 45%;
        border: 2px solid yellow;
        border-radius: 10px;
        padding: 15px;
        background: rgba(255, 255, 0, 0.1);
      }
      .list-box h3 {
        color: rgb(61, 106, 255);
        margin-bottom: 10px;
        font-size: 16px;
        text-transform: uppercase;
      }
      .list-box pre {
        color: white;
        background: none;
        margin: 0;
        font-family: monospace;
        white-space: pre-wrap;
        font-size: 14px;
      }
      .back-section {
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, 0.3);
        text-align: center;
      }
      .back-btn {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(61, 106, 255);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: rgb(61, 106, 255);
        cursor: pointer;
        margin: 10px;
        transition: all 0.2s ease;
      }
      .back-btn:hover {
        background: rgb(61, 106, 255);
        color: white;
        box-shadow: 0 0 20px rgba(0, 142, 236, 0.5);
      }
      .result-wrapper {
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
      }
      body {
        overflow: hidden;
        margin: 0;
      }
    </style>
  </head>
  <body>
    <div class="result-main-container">
      <div class="result-container">
        <h2 class="result-h2">Результат</h2>
        <div class="lists">
          <div class="list-box">
            <h3>Любимые фильмы:</h3>
            <pre>{favorites}</pre>
          </div>
          <div class="list-box">
            <h3>Недоступные фильмы:</h3>
            <pre>{invalid}</pre>
          </div>
        </div>
        <div class="back-section">
          <button class="back-btn" id="backToInputBtn">Назад</button>
          <button class="back-btn" id="toMenuBtn">В меню</button>
        </div>
      </div>
    </div>
    <script>
      (function(){
        window.backToInput = function() {
          const app = document.getElementById('app');
          app.style.transition = 'all 0.5s ease';
          app.style.opacity = '0';
          app.style.transform = 'translateY(-100%)';
          setTimeout(() => {
            const resultStyle = document.getElementById('result-style');
            if (resultStyle) resultStyle.remove();
            const resultScript = document.getElementById('result-script');
            if (resultScript) resultScript.remove();
            const taskData = window.task2Data;
            if (!taskData) {
              alert('Ошибка: исходное задание не найдено');
              return;
            }
            const taskStyle = document.createElement('style');
            taskStyle.id = 'task2-style';
            taskStyle.textContent = taskData.css || '';
            document.head.appendChild(taskStyle);
            app.className = 'task-container';
            app.innerHTML = taskData.html || '';
            const taskScript = document.createElement('script');
            taskScript.id = 'task2-script';
            taskScript.textContent = taskData.js || '';
            document.body.appendChild(taskScript);
            setTimeout(() => {
              const gen = document.getElementById('genBtn');
              if (gen && window.generateFields) gen.addEventListener('click', window.generateFields);
              const comp = document.getElementById('computeBtn');
              if (comp && window.compute) comp.addEventListener('click', window.compute);
              const menu = document.getElementById('toMenuBtn');
              if (menu && window.backToMenu) menu.addEventListener('click', window.backToMenu);
              const n = document.getElementById('n');
              if (n) n.focus();
            }, 100);
            app.style.opacity = '1';
            app.style.transform = 'translateY(0)';
            app.style.transition = '';
          }, 500);
        };
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', function(){
            const b = document.getElementById('backToInputBtn');
            if (b) b.addEventListener('click', window.backToInput);
            const m = document.getElementById('toMenuBtn');
            if (m) m.addEventListener('click', window.backToMenu);
          });
        } else {
          const b = document.getElementById('backToInputBtn');
          if (b) b.addEventListener('click', window.backToInput);
          const m = document.getElementById('toMenuBtn');
          if (m) m.addEventListener('click', window.backToMenu);
        }
        window.backToMenu = async function() {
          try {
            const responseStr = await pywebview.api.backToMain();
            const data = JSON.parse(responseStr);
            const app = document.getElementById('app') || document.body;
            const oldStyle = document.getElementById('result-style') || document.getElementById('main-style');
            if (oldStyle) oldStyle.remove();
            const oldScript = document.getElementById('result-script') || document.getElementById('main-script');
            if (oldScript) oldScript.remove();
            if (data.css) {
              const style = document.createElement('style');
              style.id = 'main-style';
              style.textContent = data.css;
              document.head.appendChild(style);
            }
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '0';
            app.style.transform = 'translateY(20px)';
            setTimeout(() => {
              app.replaceChildren();
              app.innerHTML = data.html || '';
              app.className = 'container';
              if (data.js) {
                const script = document.createElement('script');
                script.id = 'main-script';
                script.textContent = data.js;
                document.body.appendChild(script);
              }
              app.style.transform = 'translateY(-20px)';
              app.offsetHeight;
              app.style.opacity = '1';
              app.style.transform = 'translateY(0)';
              if (typeof attachHandlers === 'function') setTimeout(attachHandlers, 50);
            }, 500);
          } catch (e) {
            window.showError('Ошибка при возврате в меню: ' + (e && e.message ? e.message : String(e)));
          }
        };
      })();
    </script>
  </body>
</html>
'''

task3_txt = r'''
<html>
  <head>
    <style>
      .task-container {
        max-width: 600px;
        max-height: 80vh;
        overflow-y: auto;
        padding: 40px;
        border-radius: 25px;
        border: 2px solid #fff;
        background: rgba(0, 0, 0, .6);
        box-shadow: 0 0 25px rgba(255, 255, 255, .4);
        color: #fff;
        font-family: Arial, sans-serif;
      }
      .task-container::-webkit-scrollbar {
        width: 8px;
      }
      .task-container::-webkit-scrollbar-track {
        background: rgba(0, 0, 0, .3);
        border-top-right-radius: 25px;
        border-bottom-right-radius: 25px;
      }
      .task-container::-webkit-scrollbar-thumb {
        background: rgb(61, 106, 255);
        border-radius: 25px;
        margin: 4px 0;
      }
      .task-container::-webkit-scrollbar-thumb:hover {
        background: rgb(0, 142, 236);
      }
      .task-h2 {
        text-align: center;
        color: rgb(61, 106, 255);
        text-transform: uppercase;
        letter-spacing: 1px;
      }
      .task-label {
        font-weight: 600;
        color: #fff;
      }
      .task-input {
        padding: 10px;
        border-radius: 8px;
        border: 1px solid rgb(61, 106, 255);
        background: rgba(255, 255, 255, .1);
        color: #fff;
        margin: 5px;
        width: 200px;
      }
      .task-input::placeholder {
        color: rgba(255, 255, 255, .7);
      }
      .task-button {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(61, 106, 255);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: #fff;
        overflow: hidden;
        transition: all .2s ease-in;
        cursor: pointer;
        margin: 10px;
      }
      .task-button:hover {
        background: rgb(61, 106, 255);
        box-shadow: 0 0 20px 3px rgba(0, 142, 236, .815);
        transition: all .2s ease-out;
      }
      .back-section {
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, .3);
        text-align: center;
      }
      .error-modal {
        display: none;
        position: fixed;
        z-index: 1000;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, .8);
        backdrop-filter: blur(5px);
        opacity: 0;
        transition: opacity .3s ease;
      }
      .error-content {
        background: linear-gradient(135deg, rgba(0, 0, 0, .95), rgba(20, 20, 40, .95));
        border: 2px solid rgb(255, 61, 61);
        border-radius: 15px;
        margin: 15% auto;
        padding: 30px;
        width: 80%;
        max-width: 400px;
        color: #fff;
        text-align: center;
        box-shadow: 0 0 40px rgba(255, 61, 61, .3), inset 0 0 20px rgba(255, 255, 255, .05);
        animation: errorSlideIn .3s ease-out;
      }
      @keyframes errorSlideIn {
        from {
          transform: translateY(-50px);
          opacity: 0;
        }
        to {
          transform: translateY(0);
          opacity: 1;
        }
      }
      .error-content h3 {
        color: rgb(255, 61, 61);
        margin-bottom: 15px;
        font-size: 24px;
        text-transform: uppercase;
        letter-spacing: 1px;
      }
      .error-content p {
        font-size: 16px;
        margin-bottom: 20px;
        line-height: 1.4;
      }
      .error-close {
        color: rgba(255, 255, 255, .7);
        float: right;
        font-size: 28px;
        font-weight: 700;
        cursor: pointer;
        transition: color .2s ease;
        background: none;
        border: none;
        line-height: 1;
      }
      .error-close:hover {
        color: rgb(255, 61, 61);
      }
      .error-ok {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(255, 61, 61);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: #fff;
        cursor: pointer;
        margin-top: 10px;
        transition: all .2s ease;
      }
      .error-ok:hover {
        background: rgb(255, 61, 61);
        box-shadow: 0 0 20px 3px rgba(255, 0, 0, .5);
      }
    </style>
  </head>
  <body>
    <h2 class="task-h2">Задание 3. Бегущие цифры</h2>
    <label class="task-label">Количество элементов N:</label>
    <input type="number" id="n" min="1" class="task-input" placeholder="Введите число"><br><br>
    <button class="task-button" id="genBtn">Генерировать поля</button><br><br>
    <label class="task-label">Сдвиг K:</label>
    <input type="number" id="k" min="0" class="task-input" placeholder="Введите K"><br><br>
    <div id="fields"></div><br>
    <button class="task-button" id="computeBtn" style="display:none;">Вычислить</button>
    <div class="back-section">
      <button class="task-button" id="toMenuBtn">Назад к меню</button>
    </div>
    <script>
      (function(){
        window.originalTaskHTML = document.querySelector('.task-container') ? document.querySelector('.task-container').innerHTML : document.getElementById('app').innerHTML || '';
        if (!document.getElementById('task3-style')) {
          const s = document.createElement('style');
          s.id = 'task3-style';
          s.textContent = window.__task_css__ || '';
          document.head.appendChild(s);
        }
        window.closeModal = function(modal) {
          modal.style.opacity = '0';
          setTimeout(() => { modal.remove(); }, 300);
        };
        window.showError = function(message) {
          const modal = document.createElement('div');
          modal.className = 'error-modal';
          modal.innerHTML = `<div class="error-content"><button class="error-close" aria-label="close">&times;</button><h3>Ошибка!</h3><p>${message}</p><button class="error-ok">OK</button></div>`;
          document.body.appendChild(modal);
          modal.style.display = 'block';
          setTimeout(() => { modal.style.opacity = '1'; }, 10);
          const closeSpan = modal.querySelector('.error-close');
          closeSpan.onclick = () => closeModal(modal);
          modal.querySelector('.error-ok').onclick = () => closeModal(modal);
          modal.addEventListener('click', (e) => {
            if (e.target === modal) closeModal(modal);
          });
        };
        window.generateFields = function() {
          const nInput = document.getElementById('n');
          let n = parseInt(nInput.value);
          if (n < 1 || isNaN(n)) {
            window.showError('Введите корректное число элементов (минимум 1)');
            return;
          }
          let fields = '';
          for (let i = 1; i <= n; i++) {
            fields += `<label class="task-label">Элемент ${i}: </label><input type="number" id="num${i}" class="task-input" placeholder="Введите число"><br><br>`;
          }
          document.getElementById('fields').innerHTML = fields;
          document.getElementById('computeBtn').style.display = 'block';
          const container = document.querySelector('.task-container') || document.getElementById('app');
          if (container) container.scrollTop = 0;
        };
        window.compute = async function() {
          let n = parseInt(document.getElementById('n').value);
          let nums = [];
          let valid = true;
          for (let i = 1; i <= n; i++) {
            let val = parseInt(document.getElementById(`num${i}`).value);
            if (isNaN(val)) {
              window.showError(`Введите корректное значение для элемента ${i}`);
              valid = false;
              break;
            }
            nums.push(val);
          }
          if (!valid) return;
          let k = parseInt(document.getElementById('k').value);
          if (isNaN(k) || k < 0) {
            window.showError('Введите корректный сдвиг K (минимум 0)');
            return;
          }
          let data = { nums: nums, k: k };
          const compute_result_str = await pywebview.api.compute_task3(JSON.stringify(data));
          const compute_data = JSON.parse(compute_result_str);
          if (compute_data.error) {
            window.showError(compute_data.error);
            return;
          }
          const styleText = document.getElementById('task3-style') ? document.getElementById('task3-style').textContent : '';
          const scriptText = window.__task_js__ || '';
          const htmlText = window.originalTaskHTML || (document.querySelector('.task-container') ? document.querySelector('.task-container').innerHTML : document.getElementById('app').innerHTML);
          window.task3Data = { css: styleText, html: htmlText, js: scriptText };
          const app = document.getElementById('app');
          app.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
          app.style.opacity = '0';
          app.style.transform = 'translateY(-30px)';
          setTimeout(async () => {
            const result_response = await pywebview.api.get_task3_result_content(JSON.stringify(compute_data));
            const result_data = JSON.parse(result_response);
            let style = document.getElementById('result-style');
            if (style) style.remove();
            style = document.createElement('style');
            style.id = 'result-style';
            style.textContent = result_data.css;
            document.head.appendChild(style);
            app.className = 'result-wrapper';
            app.replaceChildren();
            app.innerHTML = result_data.html;
            let script = document.getElementById('result-script');
            if (script) script.remove();
            script = document.createElement('script');
            script.id = 'result-script';
            script.textContent = result_data.js;
            document.body.appendChild(script);
            app.style.transform = 'translateY(30px)';
            app.offsetHeight;
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '1';
            app.style.transform = 'translateY(0)';
          }, 400);
        };
        window.backToMenu = async function() {
          try {
            const responseStr = await pywebview.api.backToMain();
            const data = JSON.parse(responseStr);
            const app = document.getElementById('app') || document.body;
            const oldStyle = document.getElementById('result-style') || document.getElementById('main-style');
            if (oldStyle) oldStyle.remove();
            const oldScript = document.getElementById('result-script') || document.getElementById('main-script');
            if (oldScript) oldScript.remove();
            if (data.css) {
              const style = document.createElement('style');
              style.id = 'main-style';
              style.textContent = data.css;
              document.head.appendChild(style);
            }
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '0';
            app.style.transform = 'translateY(20px)';
            setTimeout(() => {
              app.replaceChildren();
              app.innerHTML = data.html || '';
              app.className = 'container';
              if (data.js) {
                const script = document.createElement('script');
                script.id = 'main-script';
                script.textContent = data.js;
                document.body.appendChild(script);
              }
              app.style.transform = 'translateY(-20px)';
              app.offsetHeight;
              app.style.opacity = '1';
              app.style.transform = 'translateY(0)';
              if (typeof attachHandlers === 'function') setTimeout(attachHandlers, 50);
            }, 500);
          } catch (e) {
            window.showError('Ошибка при возврате в меню: ' + (e && e.message ? e.message : String(e)));
          }
        };
        window.__task_js__ = (function(){ return `/* task js source placeholder */`; })();
        function attachHandlers(){
          const gen = document.getElementById('genBtn');
          if (gen) gen.addEventListener('click', window.generateFields);
          const comp = document.getElementById('computeBtn');
          if (comp) comp.addEventListener('click', window.compute);
          const menu = document.getElementById('toMenuBtn');
          if (menu) menu.addEventListener('click', window.backToMenu);
        }
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', attachHandlers);
        } else {
          attachHandlers();
        }
      })();
    </script>
  </body>
</html>
'''

task3_result_txt = r'''
<html>
  <head>
    <style>
      .result-main-container {
        max-width: 800px;
        padding: 40px;
        border-radius: 25px;
        border: 2px solid white;
        background: rgba(0, 0, 0, 0.6);
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.4);
        color: white;
        font-family: Arial, sans-serif;
        margin: 0 auto;
      }
      .result-container {
        text-align: center;
        padding: 20px;
      }
      .result-h2 {
        color: rgb(61, 106, 255);
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 30px;
      }
      .lists {
        display: flex;
        justify-content: space-around;
        gap: 20px;
        margin: 20px 0;
      }
      .list-box {
        flex: 1;
        max-width: 45%;
        border: 2px solid yellow;
        border-radius: 10px;
        padding: 15px;
        background: rgba(255, 255, 0, 0.1);
      }
      .list-box h3 {
        color: rgb(61, 106, 255);
        margin-bottom: 10px;
        font-size: 16px;
        text-transform: uppercase;
      }
      .list-box pre {
        color: white;
        background: none;
        margin: 0;
        font-family: monospace;
        white-space: pre-wrap;
        font-size: 14px;
      }
      .back-section {
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, 0.3);
        text-align: center;
      }
      .back-btn {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(61, 106, 255);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: rgb(61, 106, 255);
        cursor: pointer;
        margin: 10px;
        transition: all 0.2s ease;
      }
      .back-btn:hover {
        background: rgb(61, 106, 255);
        color: white;
        box-shadow: 0 0 20px rgba(0, 142, 236, 0.5);
      }
      .result-wrapper {
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
      }
      body {
        overflow: hidden;
        margin: 0;
      }
    </style>
  </head>
  <body>
    <div class="result-main-container">
      <div class="result-container">
        <h2 class="result-h2">Результат</h2>
        <div class="lists">
          <div class="list-box">
            <h3>Изначальный список:</h3>
            <pre>[ {old_list} ]</pre>
          </div>
          <div class="list-box">
            <h3>Сдвинутый список:</h3>
            <pre>[ {new_list} ]</pre>
          </div>
        </div>
        <div class="back-section">
          <button class="back-btn" id="backToInputBtn">Назад</button>
          <button class="back-btn" id="toMenuBtn">В меню</button>
        </div>
      </div>
    </div>
    <script>
      (function(){
        window.backToInput = function() {
          const app = document.getElementById('app');
          app.style.transition = 'all 0.5s ease';
          app.style.opacity = '0';
          app.style.transform = 'translateY(-100%)';
          setTimeout(() => {
            const resultStyle = document.getElementById('result-style');
            if (resultStyle) resultStyle.remove();
            const resultScript = document.getElementById('result-script');
            if (resultScript) resultScript.remove();
            const taskData = window.task3Data;
            if (!taskData) {
              alert('Ошибка: исходное задание не найдено');
              return;
            }
            const taskStyle = document.createElement('style');
            taskStyle.id = 'task3-style';
            taskStyle.textContent = taskData.css || '';
            document.head.appendChild(taskStyle);
            app.className = 'task-container';
            app.innerHTML = taskData.html || '';
            const taskScript = document.createElement('script');
            taskScript.id = 'task3-script';
            taskScript.textContent = taskData.js || '';
            document.body.appendChild(taskScript);
            setTimeout(() => {
              const gen = document.getElementById('genBtn');
              if (gen && window.generateFields) gen.addEventListener('click', window.generateFields);
              const comp = document.getElementById('computeBtn');
              if (comp && window.compute) comp.addEventListener('click', window.compute);
              const menu = document.getElementById('toMenuBtn');
              if (menu && window.backToMenu) menu.addEventListener('click', window.backToMenu);
              const n = document.getElementById('n');
              if (n) n.focus();
            }, 100);
            app.style.opacity = '1';
            app.style.transform = 'translateY(0)';
            app.style.transition = '';
          }, 500);
        };
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', function(){
            const b = document.getElementById('backToInputBtn');
            if (b) b.addEventListener('click', window.backToInput);
            const m = document.getElementById('toMenuBtn');
            if (m) m.addEventListener('click', window.backToMenu);
          });
        } else {
          const b = document.getElementById('backToInputBtn');
          if (b) b.addEventListener('click', window.backToInput);
          const m = document.getElementById('toMenuBtn');
          if (m) m.addEventListener('click', window.backToMenu);
        }
        window.backToMenu = async function() {
          try {
            const responseStr = await pywebview.api.backToMain();
            const data = JSON.parse(responseStr);
            const app = document.getElementById('app') || document.body;
            const oldStyle = document.getElementById('result-style') || document.getElementById('main-style');
            if (oldStyle) oldStyle.remove();
            const oldScript = document.getElementById('result-script') || document.getElementById('main-script');
            if (oldScript) oldScript.remove();
            if (data.css) {
              const style = document.createElement('style');
              style.id = 'main-style';
              style.textContent = data.css;
              document.head.appendChild(style);
            }
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '0';
            app.style.transform = 'translateY(20px)';
            setTimeout(() => {
              app.replaceChildren();
              app.innerHTML = data.html || '';
              app.className = 'container';
              if (data.js) {
                const script = document.createElement('script');
                script.id = 'main-script';
                script.textContent = data.js;
                document.body.appendChild(script);
              }
              app.style.transform = 'translateY(-20px)';
              app.offsetHeight;
              app.style.opacity = '1';
              app.style.transform = 'translateY(0)';
              if (typeof attachHandlers === 'function') setTimeout(attachHandlers, 50);
            }, 500);
          } catch (e) {
            window.showError('Ошибка при возврате в меню: ' + (e && e.message ? e.message : String(e)));
          }
        };
      })();
    </script>
  </body>
</html>
'''

task4_txt = r'''
<html>
  <head>
    <style>
      .task-container {
        max-width: 600px;
        max-height: 80vh;
        overflow-y: auto;
        padding: 40px;
        border-radius: 25px;
        border: 2px solid #fff;
        background: rgba(0, 0, 0, .6);
        box-shadow: 0 0 25px rgba(255, 255, 255, .4);
        color: #fff;
        font-family: Arial, sans-serif;
      }
      .task-container::-webkit-scrollbar {
        width: 8px;
      }
      .task-container::-webkit-scrollbar-track {
        background: rgba(0, 0, 0, .3);
        border-top-right-radius: 25px;
        border-bottom-right-radius: 25px;
      }
      .task-container::-webkit-scrollbar-thumb {
        background: rgb(61, 106, 255);
        border-radius: 25px;
        margin: 4px 0;
      }
      .task-container::-webkit-scrollbar-thumb:hover {
        background: rgb(0, 142, 236);
      }
      .task-h2 {
        text-align: center;
        color: rgb(61, 106, 255);
        text-transform: uppercase;
        letter-spacing: 1px;
      }
      .task-label {
        font-weight: 600;
        color: #fff;
      }
      .task-input {
        padding: 10px;
        border-radius: 8px;
        border: 1px solid rgb(61, 106, 255);
        background: rgba(255, 255, 255, .1);
        color: #fff;
        margin: 5px;
        width: 200px;
      }
      .task-input::placeholder {
        color: rgba(255, 255, 255, .7);
      }
      .task-button {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(61, 106, 255);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: #fff;
        overflow: hidden;
        transition: all .2s ease-in;
        cursor: pointer;
        margin: 10px;
      }
      .task-button:hover {
        background: rgb(61, 106, 255);
        box-shadow: 0 0 20px 3px rgba(0, 142, 236, .815);
        transition: all .2s ease-out;
      }
      .back-section {
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, .3);
        text-align: center;
      }
      .error-modal {
        display: none;
        position: fixed;
        z-index: 1000;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, .8);
        backdrop-filter: blur(5px);
        opacity: 0;
        transition: opacity .3s ease;
      }
      .error-content {
        background: linear-gradient(135deg, rgba(0, 0, 0, .95), rgba(20, 20, 40, .95));
        border: 2px solid rgb(255, 61, 61);
        border-radius: 15px;
        margin: 15% auto;
        padding: 30px;
        width: 80%;
        max-width: 400px;
        color: #fff;
        text-align: center;
        box-shadow: 0 0 40px rgba(255, 61, 61, .3), inset 0 0 20px rgba(255, 255, 255, .05);
        animation: errorSlideIn .3s ease-out;
      }
      @keyframes errorSlideIn {
        from {
          transform: translateY(-50px);
          opacity: 0;
        }
        to {
          transform: translateY(0);
          opacity: 1;
        }
      }
      .error-content h3 {
        color: rgb(255, 61, 61);
        margin-bottom: 15px;
        font-size: 24px;
        text-transform: uppercase;
        letter-spacing: 1px;
      }
      .error-content p {
        font-size: 16px;
        margin-bottom: 20px;
        line-height: 1.4;
      }
      .error-close {
        color: rgba(255, 255, 255, .7);
        float: right;
        font-size: 28px;
        font-weight: 700;
        cursor: pointer;
        transition: color .2s ease;
        background: none;
        border: none;
        line-height: 1;
      }
      .error-close:hover {
        color: rgb(255, 61, 61);
      }
      .error-ok {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(255, 61, 61);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: #fff;
        cursor: pointer;
        margin-top: 10px;
        transition: all .2s ease;
      }
      .error-ok:hover {
        background: rgb(255, 61, 61);
        box-shadow: 0 0 20px 3px rgba(255, 0, 0, .5);
      }
    </style>
  </head>
  <body>
    <h2 class="task-h2">Задание 4. Анализ слова — 2</h2>
    <label class="task-label">Введите слово:</label>
    <input type="text" id="word" class="task-input" placeholder="Введите слово"><br><br>
    <button class="task-button" id="computeBtn">Проверить</button>
    <div class="back-section">
      <button class="task-button" id="toMenuBtn">Назад к меню</button>
    </div>
    <script>
      (function(){
        window.originalTaskHTML = document.querySelector('.task-container') ? document.querySelector('.task-container').innerHTML : document.getElementById('app').innerHTML || '';
        if (!document.getElementById('task4-style')) {
          const s = document.createElement('style');
          s.id = 'task4-style';
          s.textContent = window.__task_css__ || '';
          document.head.appendChild(s);
        }
        window.closeModal = function(modal) {
          modal.style.opacity = '0';
          setTimeout(() => { modal.remove(); }, 300);
        };
        window.showError = function(message) {
          const modal = document.createElement('div');
          modal.className = 'error-modal';
          modal.innerHTML = `<div class="error-content"><button class="error-close" aria-label="close">&times;</button><h3>Ошибка!</h3><p>${message}</p><button class="error-ok">OK</button></div>`;
          document.body.appendChild(modal);
          modal.style.display = 'block';
          setTimeout(() => { modal.style.opacity = '1'; }, 10);
          const closeSpan = modal.querySelector('.error-close');
          closeSpan.onclick = () => closeModal(modal);
          modal.querySelector('.error-ok').onclick = () => closeModal(modal);
          modal.addEventListener('click', (e) => {
            if (e.target === modal) closeModal(modal);
          });
        };
        window.compute = async function() {
          let word = document.getElementById('word').value.trim();
          if (!word) {
            window.showError('Введите слово');
            return;
          }
          let data = { word: word };
          const compute_result_str = await pywebview.api.compute_task4(JSON.stringify(data));
          const compute_data = JSON.parse(compute_result_str);
          if (compute_data.error) {
            window.showError(compute_data.error);
            return;
          }
          const styleText = document.getElementById('task4-style') ? document.getElementById('task4-style').textContent : '';
          const scriptText = window.__task_js__ || '';
          const htmlText = window.originalTaskHTML || (document.querySelector('.task-container') ? document.querySelector('.task-container').innerHTML : document.getElementById('app').innerHTML);
          window.task4Data = { css: styleText, html: htmlText, js: scriptText };
          const app = document.getElementById('app');
          app.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
          app.style.opacity = '0';
          app.style.transform = 'translateY(-30px)';
          setTimeout(async () => {
            const result_response = await pywebview.api.get_task4_result_content(JSON.stringify(compute_data));
            const result_data = JSON.parse(result_response);
            let style = document.getElementById('result-style');
            if (style) style.remove();
            style = document.createElement('style');
            style.id = 'result-style';
            style.textContent = result_data.css;
            document.head.appendChild(style);
            app.className = 'result-wrapper';
            app.replaceChildren();
            app.innerHTML = result_data.html;
            let script = document.getElementById('result-script');
            if (script) script.remove();
            script = document.createElement('script');
            script.id = 'result-script';
            script.textContent = result_data.js;
            document.body.appendChild(script);
            app.style.transform = 'translateY(30px)';
            app.offsetHeight;
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '1';
            app.style.transform = 'translateY(0)';
          }, 400);
        };
        window.backToMenu = async function() {
          try {
            const responseStr = await pywebview.api.backToMain();
            const data = JSON.parse(responseStr);
            const app = document.getElementById('app') || document.body;
            const oldStyle = document.getElementById('result-style') || document.getElementById('main-style');
            if (oldStyle) oldStyle.remove();
            const oldScript = document.getElementById('result-script') || document.getElementById('main-script');
            if (oldScript) oldScript.remove();
            if (data.css) {
              const style = document.createElement('style');
              style.id = 'main-style';
              style.textContent = data.css;
              document.head.appendChild(style);
            }
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '0';
            app.style.transform = 'translateY(20px)';
            setTimeout(() => {
              app.replaceChildren();
              app.innerHTML = data.html || '';
              app.className = 'container';
              if (data.js) {
                const script = document.createElement('script');
                script.id = 'main-script';
                script.textContent = data.js;
                document.body.appendChild(script);
              }
              app.style.transform = 'translateY(-20px)';
              app.offsetHeight;
              app.style.opacity = '1';
              app.style.transform = 'translateY(0)';
              if (typeof attachHandlers === 'function') setTimeout(attachHandlers, 50);
            }, 500);
          } catch (e) {
            window.showError('Ошибка при возврате в меню: ' + (e && e.message ? e.message : String(e)));
          }
        };
        window.__task_js__ = (function(){ return `/* task js source placeholder */`; })();
        function attachHandlers(){
          const comp = document.getElementById('computeBtn');
          if (comp) comp.addEventListener('click', window.compute);
          const menu = document.getElementById('toMenuBtn');
          if (menu) menu.addEventListener('click', window.backToMenu);
          const word = document.getElementById('word');
          if (word) word.focus();
        }
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', attachHandlers);
        } else {
          attachHandlers();
        }
      })();
    </script>
  </body>
</html>
'''

task4_result_txt = r'''
<html>
  <head>
    <style>
      .result-main-container {
        max-width: 800px;
        padding: 40px;
        border-radius: 25px;
        border: 2px solid white;
        background: rgba(0, 0, 0, 0.6);
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.4);
        color: white;
        font-family: Arial, sans-serif;
        margin: 0 auto;
      }
      .result-container {
        text-align: center;
        padding: 20px;
      }
      .result-h2 {
        color: rgb(61, 106, 255);
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 30px;
      }
      .result-box {
        border: 2px solid yellow;
        border-radius: 10px;
        padding: 15px;
        background: rgba(255, 255, 0, 0.1);
        margin: 20px 0;
      }
      .result-box h3 {
        color: rgb(61, 106, 255);
        margin-bottom: 10px;
        font-size: 16px;
        text-transform: uppercase;
      }
      .result-box pre {
        color: white;
        background: none;
        margin: 0;
        font-family: monospace;
        white-space: pre-wrap;
        font-size: 14px;
      }
      .back-section {
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, 0.3);
        text-align: center;
      }
      .back-btn {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(61, 106, 255);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: rgb(61, 106, 255);
        cursor: pointer;
        margin: 10px;
        transition: all 0.2s ease;
      }
      .back-btn:hover {
        background: rgb(61, 106, 255);
        color: white;
        box-shadow: 0 0 20px rgba(0, 142, 236, 0.5);
      }
      .result-wrapper {
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
      }
      body {
        overflow: hidden;
        margin: 0;
      }
    </style>
  </head>
  <body>
    <div class="result-main-container">
      <div class="result-container">
        <h2 class="result-h2">Результат</h2>
        <div class="result-box">
          <h3>Слово:</h3>
          <pre>{word}</pre>
        </div>
        <div class="result-box">
          <h3>Статус:</h3>
          <pre>{message}</pre>
        </div>
        <div class="back-section">
          <button class="back-btn" id="backToInputBtn">Назад</button>
          <button class="back-btn" id="toMenuBtn">В меню</button>
        </div>
      </div>
    </div>
    <script>
      (function(){
        window.backToInput = function() {
          const app = document.getElementById('app');
          app.style.transition = 'all 0.5s ease';
          app.style.opacity = '0';
          app.style.transform = 'translateY(-100%)';
          setTimeout(() => {
            const resultStyle = document.getElementById('result-style');
            if (resultStyle) resultStyle.remove();
            const resultScript = document.getElementById('result-script');
            if (resultScript) resultScript.remove();
            const taskData = window.task4Data;
            if (!taskData) {
              alert('Ошибка: исходное задание не найдено');
              return;
            }
            const taskStyle = document.createElement('style');
            taskStyle.id = 'task4-style';
            taskStyle.textContent = taskData.css || '';
            document.head.appendChild(taskStyle);
            app.className = 'task-container';
            app.innerHTML = taskData.html || '';
            const taskScript = document.createElement('script');
            taskScript.id = 'task4-script';
            taskScript.textContent = taskData.js || '';
            document.body.appendChild(taskScript);
            setTimeout(() => {
              const comp = document.getElementById('computeBtn');
              if (comp && window.compute) comp.addEventListener('click', window.compute);
              const menu = document.getElementById('toMenuBtn');
              if (menu && window.backToMenu) menu.addEventListener('click', window.backToMenu);
              const word = document.getElementById('word');
              if (word) word.focus();
            }, 100);
            app.style.opacity = '1';
            app.style.transform = 'translateY(0)';
            app.style.transition = '';
          }, 500);
        };
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', function(){
            const b = document.getElementById('backToInputBtn');
            if (b) b.addEventListener('click', window.backToInput);
            const m = document.getElementById('toMenuBtn');
            if (m) m.addEventListener('click', window.backToMenu);
          });
        } else {
          const b = document.getElementById('backToInputBtn');
          if (b) b.addEventListener('click', window.backToInput);
          const m = document.getElementById('toMenuBtn');
          if (m) m.addEventListener('click', window.backToMenu);
        }
        window.backToMenu = async function() {
          try {
            const responseStr = await pywebview.api.backToMain();
            const data = JSON.parse(responseStr);
            const app = document.getElementById('app') || document.body;
            const oldStyle = document.getElementById('result-style') || document.getElementById('main-style');
            if (oldStyle) oldStyle.remove();
            const oldScript = document.getElementById('result-script') || document.getElementById('main-script');
            if (oldScript) oldScript.remove();
            if (data.css) {
              const style = document.createElement('style');
              style.id = 'main-style';
              style.textContent = data.css;
              document.head.appendChild(style);
            }
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '0';
            app.style.transform = 'translateY(20px)';
            setTimeout(() => {
              app.replaceChildren();
              app.innerHTML = data.html || '';
              app.className = 'container';
              if (data.js) {
                const script = document.createElement('script');
                script.id = 'main-script';
                script.textContent = data.js;
                document.body.appendChild(script);
              }
              app.style.transform = 'translateY(-20px)';
              app.offsetHeight;
              app.style.opacity = '1';
              app.style.transform = 'translateY(0)';
              if (typeof attachHandlers === 'function') setTimeout(attachHandlers, 50);
            }, 500);
          } catch (e) {
            window.showError('Ошибка при возврате в меню: ' + (e && e.message ? e.message : String(e)));
          }
        };
      })();
    </script>
  </body>
</html>
'''

task5_txt = r'''
<html>
  <head>
    <style>
      .task-container {
        max-width: 600px;
        max-height: 80vh;
        overflow-y: auto;
        padding: 40px;
        border-radius: 25px;
        border: 2px solid #fff;
        background: rgba(0, 0, 0, .6);
        box-shadow: 0 0 25px rgba(255, 255, 255, .4);
        color: #fff;
        font-family: Arial, sans-serif;
      }
      .task-container::-webkit-scrollbar {
        width: 8px;
      }
      .task-container::-webkit-scrollbar-track {
        background: rgba(0, 0, 0, .3);
        border-top-right-radius: 25px;
        border-bottom-right-radius: 25px;
      }
      .task-container::-webkit-scrollbar-thumb {
        background: rgb(61, 106, 255);
        border-radius: 25px;
        margin: 4px 0;
      }
      .task-container::-webkit-scrollbar-thumb:hover {
        background: rgb(0, 142, 236);
      }
      .task-h2 {
        text-align: center;
        color: rgb(61, 106, 255);
        text-transform: uppercase;
        letter-spacing: 1px;
      }
      .task-label {
        font-weight: 600;
        color: #fff;
      }
      .task-input {
        padding: 10px;
        border-radius: 8px;
        border: 1px solid rgb(61, 106, 255);
        background: rgba(255, 255, 255, .1);
        color: #fff;
        margin: 5px;
        width: 200px;
      }
      .task-input::placeholder {
        color: rgba(255, 255, 255, .7);
      }
      .task-button {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(61, 106, 255);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: #fff;
        overflow: hidden;
        transition: all .2s ease-in;
        cursor: pointer;
        margin: 10px;
      }
      .task-button:hover {
        background: rgb(61, 106, 255);
        box-shadow: 0 0 20px 3px rgba(0, 142, 236, .815);
        transition: all .2s ease-out;
      }
      .back-section {
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, .3);
        text-align: center;
      }
      .error-modal {
        display: none;
        position: fixed;
        z-index: 1000;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, .8);
        backdrop-filter: blur(5px);
        opacity: 0;
        transition: opacity .3s ease;
      }
      .error-content {
        background: linear-gradient(135deg, rgba(0, 0, 0, .95), rgba(20, 20, 40, .95));
        border: 2px solid rgb(255, 61, 61);
        border-radius: 15px;
        margin: 15% auto;
        padding: 30px;
        width: 80%;
        max-width: 400px;
        color: #fff;
        text-align: center;
        box-shadow: 0 0 40px rgba(255, 61, 61, .3), inset 0 0 20px rgba(255, 255, 255, .05);
        animation: errorSlideIn .3s ease-out;
      }
      @keyframes errorSlideIn {
        from {
          transform: translateY(-50px);
          opacity: 0;
        }
        to {
          transform: translateY(0);
          opacity: 1;
        }
      }
      .error-content h3 {
        color: rgb(255, 61, 61);
        margin-bottom: 15px;
        font-size: 24px;
        text-transform: uppercase;
        letter-spacing: 1px;
      }
      .error-content p {
        font-size: 16px;
        margin-bottom: 20px;
        line-height: 1.4;
      }
      .error-close {
        color: rgba(255, 255, 255, .7);
        float: right;
        font-size: 28px;
        font-weight: 700;
        cursor: pointer;
        transition: color .2s ease;
        background: none;
        border: none;
        line-height: 1;
      }
      .error-close:hover {
        color: rgb(255, 61, 61);
      }
      .error-ok {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(255, 61, 61);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: #fff;
        cursor: pointer;
        margin-top: 10px;
        transition: all .2s ease;
      }
      .error-ok:hover {
        background: rgb(255, 61, 61);
        box-shadow: 0 0 20px 3px rgba(255, 0, 0, .5);
      }
    </style>
  </head>
  <body>
    <h2 class="task-h2">Задание 5. Сортировка</h2>
    <label class="task-label">Количество чисел:</label>
    <input type="number" id="n" min="1" class="task-input" placeholder="Введите число"><br><br>
    <button class="task-button" id="genBtn">Генерировать поля</button><br><br>
    <div id="fields"></div><br>
    <button class="task-button" id="computeBtn" style="display:none;">Сортировать</button>
    <div class="back-section">
      <button class="task-button" id="toMenuBtn">Назад к меню</button>
    </div>
    <script>
      (function(){
        window.originalTaskHTML = document.querySelector('.task-container') ? document.querySelector('.task-container').innerHTML : document.getElementById('app').innerHTML || '';
        if (!document.getElementById('task5-style')) {
          const s = document.createElement('style');
          s.id = 'task5-style';
          s.textContent = window.__task_css__ || '';
          document.head.appendChild(s);
        }
        window.closeModal = function(modal) {
          modal.style.opacity = '0';
          setTimeout(() => { modal.remove(); }, 300);
        };
        window.showError = function(message) {
          const modal = document.createElement('div');
          modal.className = 'error-modal';
          modal.innerHTML = `<div class="error-content"><button class="error-close" aria-label="close">&times;</button><h3>Ошибка!</h3><p>${message}</p><button class="error-ok">OK</button></div>`;
          document.body.appendChild(modal);
          modal.style.display = 'block';
          setTimeout(() => { modal.style.opacity = '1'; }, 10);
          const closeSpan = modal.querySelector('.error-close');
          closeSpan.onclick = () => closeModal(modal);
          modal.querySelector('.error-ok').onclick = () => closeModal(modal);
          modal.addEventListener('click', (e) => {
            if (e.target === modal) closeModal(modal);
          });
        };
        window.generateFields = function() {
          const nInput = document.getElementById('n');
          let n = parseInt(nInput.value);
          if (n < 1 || isNaN(n)) {
            window.showError('Введите корректное число (минимум 1)');
            return;
          }
          let fields = '';
          for (let i = 1; i <= n; i++) {
            fields += `<label class="task-label">Число ${i}: </label><input type="number" id="num${i}" class="task-input" placeholder="Введите число"><br><br>`;
          }
          document.getElementById('fields').innerHTML = fields;
          document.getElementById('computeBtn').style.display = 'block';
          const container = document.querySelector('.task-container') || document.getElementById('app');
          if (container) container.scrollTop = 0;
        };
        window.compute = async function() {
          let n = parseInt(document.getElementById('n').value);
          let numbers = [];
          let valid = true;
          for (let i = 1; i <= n; i++) {
            let val = parseInt(document.getElementById(`num${i}`).value);
            if (isNaN(val)) {
              window.showError(`Введите корректное значение для числа ${i}`);
              valid = false;
              break;
            }
            numbers.push(val);
          }
          if (!valid) return;
          let data = { numbers: numbers };
          const compute_result_str = await pywebview.api.compute_task5(JSON.stringify(data));
          const compute_data = JSON.parse(compute_result_str);
          if (compute_data.error) {
            window.showError(compute_data.error);
            return;
          }
          const styleText = document.getElementById('task5-style') ? document.getElementById('task5-style').textContent : '';
          const scriptText = window.__task_js__ || '';
          const htmlText = window.originalTaskHTML || (document.querySelector('.task-container') ? document.querySelector('.task-container').innerHTML : document.getElementById('app').innerHTML);
          window.task5Data = { css: styleText, html: htmlText, js: scriptText };
          const app = document.getElementById('app');
          app.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
          app.style.opacity = '0';
          app.style.transform = 'translateY(-30px)';
          setTimeout(async () => {
            const result_response = await pywebview.api.get_task5_result_content(JSON.stringify(compute_data));
            const result_data = JSON.parse(result_response);
            let style = document.getElementById('result-style');
            if (style) style.remove();
            style = document.createElement('style');
            style.id = 'result-style';
            style.textContent = result_data.css;
            document.head.appendChild(style);
            app.className = 'result-wrapper';
            app.replaceChildren();
            app.innerHTML = result_data.html;
            let script = document.getElementById('result-script');
            if (script) script.remove();
            script = document.createElement('script');
            script.id = 'result-script';
            script.textContent = result_data.js;
            document.body.appendChild(script);
            app.style.transform = 'translateY(30px)';
            app.offsetHeight;
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '1';
            app.style.transform = 'translateY(0)';
          }, 400);
        };
        window.backToMenu = async function() {
          try {
            const responseStr = await pywebview.api.backToMain();
            const data = JSON.parse(responseStr);
            const app = document.getElementById('app') || document.body;
            const oldStyle = document.getElementById('result-style') || document.getElementById('main-style');
            if (oldStyle) oldStyle.remove();
            const oldScript = document.getElementById('result-script') || document.getElementById('main-script');
            if (oldScript) oldScript.remove();
            if (data.css) {
              const style = document.createElement('style');
              style.id = 'main-style';
              style.textContent = data.css;
              document.head.appendChild(style);
            }
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '0';
            app.style.transform = 'translateY(20px)';
            setTimeout(() => {
              app.replaceChildren();
              app.innerHTML = data.html || '';
              app.className = 'container';
              if (data.js) {
                const script = document.createElement('script');
                script.id = 'main-script';
                script.textContent = data.js;
                document.body.appendChild(script);
              }
              app.style.transform = 'translateY(-20px)';
              app.offsetHeight;
              app.style.opacity = '1';
              app.style.transform = 'translateY(0)';
              if (typeof attachHandlers === 'function') setTimeout(attachHandlers, 50);
            }, 500);
          } catch (e) {
            window.showError('Ошибка при возврате в меню: ' + (e && e.message ? e.message : String(e)));
          }
        };
        window.__task_js__ = (function(){ return `/* task js source placeholder */`; })();
        function attachHandlers(){
          const gen = document.getElementById('genBtn');
          if (gen) gen.addEventListener('click', window.generateFields);
          const comp = document.getElementById('computeBtn');
          if (comp) comp.addEventListener('click', window.compute);
          const menu = document.getElementById('toMenuBtn');
          if (menu) menu.addEventListener('click', window.backToMenu);
          const n = document.getElementById('n');
          if (n) n.focus();
        }
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', attachHandlers);
        } else {
          attachHandlers();
        }
      })();
    </script>
  </body>
</html>
'''

task5_result_txt = r'''
<html>
  <head>
    <style>
      .result-main-container {
        max-width: 800px;
        padding: 40px;
        border-radius: 25px;
        border: 2px solid white;
        background: rgba(0, 0, 0, 0.6);
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.4);
        color: white;
        font-family: Arial, sans-serif;
        margin: 0 auto;
      }
      .result-container {
        text-align: center;
        padding: 20px;
      }
      .result-h2 {
        color: rgb(61, 106, 255);
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 30px;
      }
      .lists {
        display: flex;
        justify-content: space-around;
        gap: 20px;
        margin: 20px 0;
      }
      .list-box {
        flex: 1;
        max-width: 45%;
        border: 2px solid yellow;
        border-radius: 10px;
        padding: 15px;
        background: rgba(255, 255, 0, 0.1);
      }
      .list-box h3 {
        color: rgb(61, 106, 255);
        margin-bottom: 10px;
        font-size: 16px;
        text-transform: uppercase;
      }
      .list-box pre {
        color: white;
        background: none;
        margin: 0;
        font-family: monospace;
        white-space: pre-wrap;
        font-size: 14px;
      }
      .back-section {
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, 0.3);
        text-align: center;
      }
      .back-btn {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(61, 106, 255);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: rgb(61, 106, 255);
        cursor: pointer;
        margin: 10px;
        transition: all 0.2s ease;
      }
      .back-btn:hover {
        background: rgb(61, 106, 255);
        color: white;
        box-shadow: 0 0 20px rgba(0, 142, 236, 0.5);
      }
      .result-wrapper {
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
      }
      body {
        overflow: hidden;
        margin: 0;
      }
    </style>
  </head>
  <body>
    <div class="result-main-container">
      <div class="result-container">
        <h2 class="result-h2">Результат</h2>
        <div class="lists">
          <div class="list-box">
            <h3>Изначальный список:</h3>
            <pre>[ {old_list} ]</pre>
          </div>
          <div class="list-box">
            <h3>Отсортированный список:</h3>
            <pre>[ {new_list} ]</pre>
          </div>
        </div>
        <div class="back-section">
          <button class="back-btn" id="backToInputBtn">Назад</button>
          <button class="back-btn" id="toMenuBtn">В меню</button>
        </div>
      </div>
    </div>
    <script>
      (function(){
        window.backToInput = function() {
          const app = document.getElementById('app');
          app.style.transition = 'all 0.5s ease';
          app.style.opacity = '0';
          app.style.transform = 'translateY(-100%)';
          setTimeout(() => {
            const resultStyle = document.getElementById('result-style');
            if (resultStyle) resultStyle.remove();
            const resultScript = document.getElementById('result-script');
            if (resultScript) resultScript.remove();
            const taskData = window.task5Data;
            if (!taskData) {
              alert('Ошибка: исходное задание не найдено');
              return;
            }
            const taskStyle = document.createElement('style');
            taskStyle.id = 'task5-style';
            taskStyle.textContent = taskData.css || '';
            document.head.appendChild(taskStyle);
            app.className = 'task-container';
            app.innerHTML = taskData.html || '';
            const taskScript = document.createElement('script');
            taskScript.id = 'task5-script';
            taskScript.textContent = taskData.js || '';
            document.body.appendChild(taskScript);
            setTimeout(() => {
              const gen = document.getElementById('genBtn');
              if (gen && window.generateFields) gen.addEventListener('click', window.generateFields);
              const comp = document.getElementById('computeBtn');
              if (comp && window.compute) comp.addEventListener('click', window.compute);
              const menu = document.getElementById('toMenuBtn');
              if (menu && window.backToMenu) menu.addEventListener('click', window.backToMenu);
              const n = document.getElementById('n');
              if (n) n.focus();
            }, 100);
            app.style.opacity = '1';
            app.style.transform = 'translateY(0)';
            app.style.transition = '';
          }, 500);
        };
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', function(){
            const b = document.getElementById('backToInputBtn');
            if (b) b.addEventListener('click', window.backToInput);
            const m = document.getElementById('toMenuBtn');
            if (m) m.addEventListener('click', window.backToMenu);
          });
        } else {
          const b = document.getElementById('backToInputBtn');
          if (b) b.addEventListener('click', window.backToInput);
          const m = document.getElementById('toMenuBtn');
          if (m) m.addEventListener('click', window.backToMenu);
        }
        window.backToMenu = async function() {
          try {
            const responseStr = await pywebview.api.backToMain();
            const data = JSON.parse(responseStr);
            const app = document.getElementById('app') || document.body;
            const oldStyle = document.getElementById('result-style') || document.getElementById('main-style');
            if (oldStyle) oldStyle.remove();
            const oldScript = document.getElementById('result-script') || document.getElementById('main-script');
            if (oldScript) oldScript.remove();
            if (data.css) {
              const style = document.createElement('style');
              style.id = 'main-style';
              style.textContent = data.css;
              document.head.appendChild(style);
            }
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '0';
            app.style.transform = 'translateY(20px)';
            setTimeout(() => {
              app.replaceChildren();
              app.innerHTML = data.html || '';
              app.className = 'container';
              if (data.js) {
                const script = document.createElement('script');
                script.id = 'main-script';
                script.textContent = data.js;
                document.body.appendChild(script);
              }
              app.style.transform = 'translateY(-20px)';
              app.offsetHeight;
              app.style.opacity = '1';
              app.style.transform = 'translateY(0)';
              if (typeof attachHandlers === 'function') setTimeout(attachHandlers, 50);
            }, 500);
          } catch (e) {
            window.showError('Ошибка при возврате в меню: ' + (e && e.message ? e.message : String(e)));
          }
        };
      })();
    </script>
  </body>
</html>
'''

task6_txt = r'''
<html>
  <head>
    <style>
      .task-container {
        max-width: 600px;
        max-height: 80vh;
        overflow-y: auto;
        padding: 40px;
        border-radius: 25px;
        border: 2px solid #fff;
        background: rgba(0, 0, 0, .6);
        box-shadow: 0 0 25px rgba(255, 255, 255, .4);
        color: #fff;
        font-family: Arial, sans-serif;
      }
      .task-container::-webkit-scrollbar {
        width: 8px;
      }
      .task-container::-webkit-scrollbar-track {
        background: rgba(0, 0, 0, .3);
        border-top-right-radius: 25px;
        border-bottom-right-radius: 25px;
      }
      .task-container::-webkit-scrollbar-thumb {
        background: rgb(61, 106, 255);
        border-radius: 25px;
        margin: 4px 0;
      }
      .task-container::-webkit-scrollbar-thumb:hover {
        background: rgb(0, 142, 236);
      }
      .task-h2 {
        text-align: center;
        color: rgb(61, 106, 255);
        text-transform: uppercase;
        letter-spacing: 1px;
      }
      .task-label {
        font-weight: 600;
        color: #fff;
      }
      .task-input {
        padding: 10px;
        border-radius: 8px;
        border: 1px solid rgb(61, 106, 255);
        background: rgba(255, 255, 255, .1);
        color: #fff;
        margin: 5px;
        width: 200px;
      }
      .task-input::placeholder {
        color: rgba(255, 255, 255, .7);
      }
      .task-button {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(61, 106, 255);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: #fff;
        overflow: hidden;
        transition: all .2s ease-in;
        cursor: pointer;
        margin: 10px;
      }
      .task-button:hover {
        background: rgb(61, 106, 255);
        box-shadow: 0 0 20px 3px rgba(0, 142, 236, .815);
        transition: all .2s ease-out;
      }
      .back-section {
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, .3);
        text-align: center;
      }
      .error-modal {
        display: none;
        position: fixed;
        z-index: 1000;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, .8);
        backdrop-filter: blur(5px);
        opacity: 0;
        transition: opacity .3s ease;
      }
      .error-content {
        background: linear-gradient(135deg, rgba(0, 0, 0, .95), rgba(20, 20, 40, .95));
        border: 2px solid rgb(255, 61, 61);
        border-radius: 15px;
        margin: 15% auto;
        padding: 30px;
        width: 80%;
        max-width: 400px;
        color: #fff;
        text-align: center;
        box-shadow: 0 0 40px rgba(255, 61, 61, .3), inset 0 0 20px rgba(255, 255, 255, .05);
        animation: errorSlideIn .3s ease-out;
      }
      @keyframes errorSlideIn {
        from {
          transform: translateY(-50px);
          opacity: 0;
        }
        to {
          transform: translateY(0);
          opacity: 1;
        }
      }
      .error-content h3 {
        color: rgb(255, 61, 61);
        margin-bottom: 15px;
        font-size: 24px;
        text-transform: uppercase;
        letter-spacing: 1px;
      }
      .error-content p {
        font-size: 16px;
        margin-bottom: 20px;
        line-height: 1.4;
      }
      .error-close {
        color: rgba(255, 255, 255, .7);
        float: right;
        font-size: 28px;
        font-weight: 700;
        cursor: pointer;
        transition: color .2s ease;
        background: none;
        border: none;
        line-height: 1;
      }
      .error-close:hover {
        color: rgb(255, 61, 61);
      }
      .error-ok {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(255, 61, 61);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: #fff;
        cursor: pointer;
        margin-top: 10px;
        transition: all .2s ease;
      }
      .error-ok:hover {
        background: rgb(255, 61, 61);
        box-shadow: 0 0 20px 3px rgba(255, 0, 0, .5);
      }
      .list-section {
        margin: 20px 0;
      }
    </style>
  </head>
  <body>
    <h2 class="task-h2">Задание 6. Уникальное объединение списков</h2>
    <div class="list-section">
      <label class="task-label">Количество элементов в первом списке:</label>
      <input type="number" id="n1" min="1" class="task-input" placeholder="Введите число"><br><br>
      <button class="task-button" id="genBtn1">Генерировать поля для списка 1</button><br><br>
      <div id="fields1"></div><br>
    </div>
    <div class="list-section">
      <label class="task-label">Количество элементов во втором списке:</label>
      <input type="number" id="n2" min="1" class="task-input" placeholder="Введите число"><br><br>
      <button class="task-button" id="genBtn2">Генерировать поля для списка 2</button><br><br>
      <div id="fields2"></div><br>
    </div>
    <button class="task-button" id="computeBtn" style="display:none;">Объединить</button>
    <div class="back-section">
      <button class="task-button" id="toMenuBtn">Назад к меню</button>
    </div>
    <script>
      (function(){
        window.originalTaskHTML = document.querySelector('.task-container') ? document.querySelector('.task-container').innerHTML : document.getElementById('app').innerHTML || '';
        if (!document.getElementById('task6-style')) {
          const s = document.createElement('style');
          s.id = 'task6-style';
          s.textContent = window.__task_css__ || '';
          document.head.appendChild(s);
        }
        window.closeModal = function(modal) {
          modal.style.opacity = '0';
          setTimeout(() => { modal.remove(); }, 300);
        };
        window.showError = function(message) {
          const modal = document.createElement('div');
          modal.className = 'error-modal';
          modal.innerHTML = `<div class="error-content"><button class="error-close" aria-label="close">&times;</button><h3>Ошибка!</h3><p>${message}</p><button class="error-ok">OK</button></div>`;
          document.body.appendChild(modal);
          modal.style.display = 'block';
          setTimeout(() => { modal.style.opacity = '1'; }, 10);
          const closeSpan = modal.querySelector('.error-close');
          closeSpan.onclick = () => closeModal(modal);
          modal.querySelector('.error-ok').onclick = () => closeModal(modal);
          modal.addEventListener('click', (e) => {
            if (e.target === modal) closeModal(modal);
          });
        };
        window.generateList1 = function() {
          const n1Input = document.getElementById('n1');
          let n1 = parseInt(n1Input.value);
          if (n1 < 1 || isNaN(n1)) {
            window.showError('Введите корректное число для списка 1 (минимум 1)');
            return;
          }
          let fields = '';
          for (let i = 1; i <= n1; i++) {
            fields += `<label class="task-label">Элемент ${i} списка 1: </label><input type="number" id="num1_${i}" class="task-input" placeholder="Введите число"><br><br>`;
          }
          document.getElementById('fields1').innerHTML = fields;
          if (document.getElementById('fields2').innerHTML.trim() !== '') {
            document.getElementById('computeBtn').style.display = 'block';
          }
        };
        window.generateList2 = function() {
          const n2Input = document.getElementById('n2');
          let n2 = parseInt(n2Input.value);
          if (n2 < 1 || isNaN(n2)) {
            window.showError('Введите корректное число для списка 2 (минимум 1)');
            return;
          }
          let fields = '';
          for (let i = 1; i <= n2; i++) {
            fields += `<label class="task-label">Элемент ${i} списка 2: </label><input type="number" id="num2_${i}" class="task-input" placeholder="Введите число"><br><br>`;
          }
          document.getElementById('fields2').innerHTML = fields;
          if (document.getElementById('fields1').innerHTML.trim() !== '') {
            document.getElementById('computeBtn').style.display = 'block';
          }
        };
        window.compute = async function() {
          let list1 = [];
          let list2 = [];
          let valid = true;
          if (document.getElementById('fields1').innerHTML.trim() === '') {
            window.showError('Генерируйте поля для списка 1');
            return;
          }
          let n1 = parseInt(document.getElementById('n1').value);
          for (let i = 1; i <= n1; i++) {
            let val = parseInt(document.getElementById(`num1_${i}`).value);
            if (isNaN(val)) {
              window.showError(`Введите значение для элемента ${i} списка 1`);
              valid = false;
              break;
            }
            list1.push(val);
          }
          if (!valid) return;
          if (document.getElementById('fields2').innerHTML.trim() === '') {
            window.showError('Генерируйте поля для списка 2');
            return;
          }
          let n2 = parseInt(document.getElementById('n2').value);
          for (let i = 1; i <= n2; i++) {
            let val = parseInt(document.getElementById(`num2_${i}`).value);
            if (isNaN(val)) {
              window.showError(`Введите значение для элемента ${i} списка 2`);
              valid = false;
              break;
            }
            list2.push(val);
          }
          if (!valid) return;
          let data = { list1: list1, list2: list2 };
          const compute_result_str = await pywebview.api.compute_task6(JSON.stringify(data));
          const compute_data = JSON.parse(compute_result_str);
          if (compute_data.error) {
            window.showError(compute_data.error);
            return;
          }
          const styleText = document.getElementById('task6-style') ? document.getElementById('task6-style').textContent : '';
          const scriptText = window.__task_js__ || '';
          const htmlText = window.originalTaskHTML || (document.querySelector('.task-container') ? document.querySelector('.task-container').innerHTML : document.getElementById('app').innerHTML);
          window.task6Data = { css: styleText, html: htmlText, js: scriptText };
          const app = document.getElementById('app');
          app.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
          app.style.opacity = '0';
          app.style.transform = 'translateY(-30px)';
          setTimeout(async () => {
            const result_response = await pywebview.api.get_task6_result_content(JSON.stringify(compute_data));
            const result_data = JSON.parse(result_response);
            let style = document.getElementById('result-style');
            if (style) style.remove();
            style = document.createElement('style');
            style.id = 'result-style';
            style.textContent = result_data.css;
            document.head.appendChild(style);
            app.className = 'result-wrapper';
            app.replaceChildren();
            app.innerHTML = result_data.html;
            let script = document.getElementById('result-script');
            if (script) script.remove();
            script = document.createElement('script');
            script.id = 'result-script';
            script.textContent = result_data.js;
            document.body.appendChild(script);
            app.style.transform = 'translateY(30px)';
            app.offsetHeight;
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '1';
            app.style.transform = 'translateY(0)';
          }, 400);
        };
        window.backToMenu = async function() {
          try {
            const responseStr = await pywebview.api.backToMain();
            const data = JSON.parse(responseStr);
            const app = document.getElementById('app') || document.body;
            const oldStyle = document.getElementById('result-style') || document.getElementById('main-style');
            if (oldStyle) oldStyle.remove();
            const oldScript = document.getElementById('result-script') || document.getElementById('main-script');
            if (oldScript) oldScript.remove();
            if (data.css) {
              const style = document.createElement('style');
              style.id = 'main-style';
              style.textContent = data.css;
              document.head.appendChild(style);
            }
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '0';
            app.style.transform = 'translateY(20px)';
            setTimeout(() => {
              app.replaceChildren();
              app.innerHTML = data.html || '';
              app.className = 'container';
              if (data.js) {
                const script = document.createElement('script');
                script.id = 'main-script';
                script.textContent = data.js;
                document.body.appendChild(script);
              }
              app.style.transform = 'translateY(-20px)';
              app.offsetHeight;
              app.style.opacity = '1';
              app.style.transform = 'translateY(0)';
              if (typeof attachHandlers === 'function') setTimeout(attachHandlers, 50);
            }, 500);
          } catch (e) {
            window.showError('Ошибка при возврате в меню: ' + (e && e.message ? e.message : String(e)));
          }
        };
        window.__task_js__ = (function(){ return `/* task js source placeholder */`; })();
        function attachHandlers(){
          const gen1 = document.getElementById('genBtn1');
          if (gen1) gen1.addEventListener('click', window.generateList1);
          const gen2 = document.getElementById('genBtn2');
          if (gen2) gen2.addEventListener('click', window.generateList2);
          const comp = document.getElementById('computeBtn');
          if (comp) comp.addEventListener('click', window.compute);
          const menu = document.getElementById('toMenuBtn');
          if (menu) menu.addEventListener('click', window.backToMenu);
          const n1 = document.getElementById('n1');
          if (n1) n1.focus();
        }
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', attachHandlers);
        } else {
          attachHandlers();
        }
      })();
    </script>
  </body>
</html>
'''

task6_result_txt = r'''
<html>
  <head>
    <style>
      .result-main-container {
        max-width: 800px;
        padding: 40px;
        border-radius: 25px;
        border: 2px solid white;
        background: rgba(0, 0, 0, 0.6);
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.4);
        color: white;
        font-family: Arial, sans-serif;
        margin: 0 auto;
      }
      .result-container {
        text-align: center;
        padding: 20px;
      }
      .result-h2 {
        color: rgb(61, 106, 255);
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 30px;
      }
      .list-box {
        border: 2px solid yellow;
        border-radius: 10px;
        padding: 15px;
        background: rgba(255, 255, 0, 0.1);
        margin: 20px 0;
      }
      .list-box h3 {
        color: rgb(61, 106, 255);
        margin-bottom: 10px;
        font-size: 16px;
        text-transform: uppercase;
      }
      .list-box pre {
        color: white;
        background: none;
        margin: 0;
        font-family: monospace;
        white-space: pre-wrap;
        font-size: 14px;
      }
      .back-section {
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, 0.3);
        text-align: center;
      }
      .back-btn {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(61, 106, 255);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: rgb(61, 106, 255);
        cursor: pointer;
        margin: 10px;
        transition: all 0.2s ease;
      }
      .back-btn:hover {
        background: rgb(61, 106, 255);
        color: white;
        box-shadow: 0 0 20px rgba(0, 142, 236, 0.5);
      }
      .result-wrapper {
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
      }
      body {
        overflow: hidden;
        margin: 0;
      }
    </style>
  </head>
  <body>
    <div class="result-main-container">
      <div class="result-container">
        <h2 class="result-h2">Результат</h2>
        <div class="list-box">
          <h3>Объединенный список:</h3>
          <pre>[ {merged_list} ]</pre>
        </div>
        <div class="back-section">
          <button class="back-btn" id="backToInputBtn">Назад</button>
          <button class="back-btn" id="toMenuBtn">В меню</button>
        </div>
      </div>
    </div>
    <script>
      (function(){
        window.backToInput = function() {
          const app = document.getElementById('app');
          app.style.transition = 'all 0.5s ease';
          app.style.opacity = '0';
          app.style.transform = 'translateY(-100%)';
          setTimeout(() => {
            const resultStyle = document.getElementById('result-style');
            if (resultStyle) resultStyle.remove();
            const resultScript = document.getElementById('result-script');
            if (resultScript) resultScript.remove();
            const taskData = window.task6Data;
            if (!taskData) {
              alert('Ошибка: исходное задание не найдено');
              return;
            }
            const taskStyle = document.createElement('style');
            taskStyle.id = 'task6-style';
            taskStyle.textContent = taskData.css || '';
            document.head.appendChild(taskStyle);
            app.className = 'task-container';
            app.innerHTML = taskData.html || '';
            const taskScript = document.createElement('script');
            taskScript.id = 'task6-script';
            taskScript.textContent = taskData.js || '';
            document.body.appendChild(taskScript);
            setTimeout(() => {
              const gen1 = document.getElementById('genBtn1');
              if (gen1 && window.generateList1) gen1.addEventListener('click', window.generateList1);
              const gen2 = document.getElementById('genBtn2');
              if (gen2 && window.generateList2) gen2.addEventListener('click', window.generateList2);
              const comp = document.getElementById('computeBtn');
              if (comp && window.compute) comp.addEventListener('click', window.compute);
              const menu = document.getElementById('toMenuBtn');
              if (menu && window.backToMenu) menu.addEventListener('click', window.backToMenu);
              const n1 = document.getElementById('n1');
              if (n1) n1.focus();
            }, 100);
            app.style.opacity = '1';
            app.style.transform = 'translateY(0)';
            app.style.transition = '';
          }, 500);
        };
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', function(){
            const b = document.getElementById('backToInputBtn');
            if (b) b.addEventListener('click', window.backToInput);
            const m = document.getElementById('toMenuBtn');
            if (m) m.addEventListener('click', window.backToMenu);
          });
        } else {
          const b = document.getElementById('backToInputBtn');
          if (b) b.addEventListener('click', window.backToInput);
          const m = document.getElementById('toMenuBtn');
          if (m) m.addEventListener('click', window.backToMenu);
        }
        window.backToMenu = async function() {
          try {
            const responseStr = await pywebview.api.backToMain();
            const data = JSON.parse(responseStr);
            const app = document.getElementById('app') || document.body;
            const oldStyle = document.getElementById('result-style') || document.getElementById('main-style');
            if (oldStyle) oldStyle.remove();
            const oldScript = document.getElementById('result-script') || document.getElementById('main-script');
            if (oldScript) oldScript.remove();
            if (data.css) {
              const style = document.createElement('style');
              style.id = 'main-style';
              style.textContent = data.css;
              document.head.appendChild(style);
            }
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '0';
            app.style.transform = 'translateY(20px)';
            setTimeout(() => {
              app.replaceChildren();
              app.innerHTML = data.html || '';
              app.className = 'container';
              if (data.js) {
                const script = document.createElement('script');
                script.id = 'main-script';
                script.textContent = data.js;
                document.body.appendChild(script);
              }
              app.style.transform = 'translateY(-20px)';
              app.offsetHeight;
              app.style.opacity = '1';
              app.style.transform = 'translateY(0)';
              if (typeof attachHandlers === 'function') setTimeout(attachHandlers, 50);
            }, 500);
          } catch (e) {
            window.showError('Ошибка при возврате в меню: ' + (e && e.message ? e.message : String(e)));
          }
        };
      })();
    </script>
  </body>
</html>
'''

task7_txt = r'''
<html>
  <head>
    <style>
      .task-container {
        max-width: 600px;
        max-height: 80vh;
        overflow-y: auto;
        padding: 40px;
        border-radius: 25px;
        border: 2px solid #fff;
        background: rgba(0, 0, 0, .6);
        box-shadow: 0 0 25px rgba(255, 255, 255, .4);
        color: #fff;
        font-family: Arial, sans-serif;
      }
      .task-container::-webkit-scrollbar {
        width: 8px;
      }
      .task-container::-webkit-scrollbar-track {
        background: rgba(0, 0, 0, .3);
        border-top-right-radius: 25px;
        border-bottom-right-radius: 25px;
      }
      .task-container::-webkit-scrollbar-thumb {
        background: rgb(61, 106, 255);
        border-radius: 25px;
        margin: 4px 0;
      }
      .task-container::-webkit-scrollbar-thumb:hover {
        background: rgb(0, 142, 236);
      }
      .task-h2 {
        text-align: center;
        color: rgb(61, 106, 255);
        text-transform: uppercase;
        letter-spacing: 1px;
      }
      .task-label {
        font-weight: 600;
        color: #fff;
      }
      .task-input {
        padding: 10px;
        border-radius: 8px;
        border: 1px solid rgb(61, 106, 255);
        background: rgba(255, 255, 255, .1);
        color: #fff;
        margin: 5px;
        width: 200px;
      }
      .task-input::placeholder {
        color: rgba(255, 255, 255, .7);
      }
      .task-button {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(61, 106, 255);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: #fff;
        overflow: hidden;
        transition: all .2s ease-in;
        cursor: pointer;
        margin: 10px;
      }
      .task-button:hover {
        background: rgb(61, 106, 255);
        box-shadow: 0 0 20px 3px rgba(0, 142, 236, .815);
        transition: all .2s ease-out;
      }
      .back-section {
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, .3);
        text-align: center;
      }
      .error-modal {
        display: none;
        position: fixed;
        z-index: 1000;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, .8);
        backdrop-filter: blur(5px);
        opacity: 0;
        transition: opacity .3s ease;
      }
      .error-content {
        background: linear-gradient(135deg, rgba(0, 0, 0, .95), rgba(20, 20, 40, .95));
        border: 2px solid rgb(255, 61, 61);
        border-radius: 15px;
        margin: 15% auto;
        padding: 30px;
        width: 80%;
        max-width: 400px;
        color: #fff;
        text-align: center;
        box-shadow: 0 0 40px rgba(255, 61, 61, .3), inset 0 0 20px rgba(255, 255, 255, .05);
        animation: errorSlideIn .3s ease-out;
      }
      @keyframes errorSlideIn {
        from {
          transform: translateY(-50px);
          opacity: 0;
        }
        to {
          transform: translateY(0);
          opacity: 1;
        }
      }
      .error-content h3 {
        color: rgb(255, 61, 61);
        margin-bottom: 15px;
        font-size: 24px;
        text-transform: uppercase;
        letter-spacing: 1px;
      }
      .error-content p {
        font-size: 16px;
        margin-bottom: 20px;
        line-height: 1.4;
      }
      .error-close {
        color: rgba(255, 255, 255, .7);
        float: right;
        font-size: 28px;
        font-weight: 700;
        cursor: pointer;
        transition: color .2s ease;
        background: none;
        border: none;
        line-height: 1;
      }
      .error-close:hover {
        color: rgb(255, 61, 61);
      }
      .error-ok {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(255, 61, 61);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: #fff;
        cursor: pointer;
        margin-top: 10px;
        transition: all .2s ease;
      }
      .error-ok:hover {
        background: rgb(255, 61, 61);
        box-shadow: 0 0 20px 3px rgba(255, 0, 0, .5);
      }
    </style>
  </head>
  <body>
    <h2 class="task-h2">Задание 7. Детали</h2>
    <label class="task-label">Название детали:</label>
    <input type="text" id="detail" class="task-input" placeholder="Введите название"><br><br>
    <button class="task-button" id="computeBtn">Вычислить</button>
    <div class="back-section">
      <button class="task-button" id="toMenuBtn">Назад к меню</button>
    </div>
    <script>
      (function(){
        window.originalTaskHTML = document.querySelector('.task-container') ? document.querySelector('.task-container').innerHTML : document.getElementById('app').innerHTML || '';
        if (!document.getElementById('task7-style')) {
          const s = document.createElement('style');
          s.id = 'task7-style';
          s.textContent = window.__task_css__ || '';
          document.head.appendChild(s);
        }
        window.closeModal = function(modal) {
          modal.style.opacity = '0';
          setTimeout(() => { modal.remove(); }, 300);
        };
        window.showError = function(message) {
          const modal = document.createElement('div');
          modal.className = 'error-modal';
          modal.innerHTML = `<div class="error-content"><button class="error-close" aria-label="close">&times;</button><h3>Ошибка!</h3><p>${message}</p><button class="error-ok">OK</button></div>`;
          document.body.appendChild(modal);
          modal.style.display = 'block';
          setTimeout(() => { modal.style.opacity = '1'; }, 10);
          const closeSpan = modal.querySelector('.error-close');
          closeSpan.onclick = () => closeModal(modal);
          modal.querySelector('.error-ok').onclick = () => closeModal(modal);
          modal.addEventListener('click', (e) => {
            if (e.target === modal) closeModal(modal);
          });
        };
        window.compute = async function() {
          let detail = document.getElementById('detail').value.trim();
          if (!detail) {
            window.showError('Введите название детали');
            return;
          }
          let data = { detail: detail };
          const compute_result_str = await pywebview.api.compute_task7(JSON.stringify(data));
          const compute_data = JSON.parse(compute_result_str);
          if (compute_data.error) {
            window.showError(compute_data.error);
            return;
          }
          const styleText = document.getElementById('task7-style') ? document.getElementById('task7-style').textContent : '';
          const scriptText = window.__task_js__ || '';
          const htmlText = window.originalTaskHTML || (document.querySelector('.task-container') ? document.querySelector('.task-container').innerHTML : document.getElementById('app').innerHTML);
          window.task7Data = { css: styleText, html: htmlText, js: scriptText };
          const app = document.getElementById('app');
          app.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
          app.style.opacity = '0';
          app.style.transform = 'translateY(-30px)';
          setTimeout(async () => {
            const result_response = await pywebview.api.get_task7_result_content(JSON.stringify(compute_data));
            const result_data = JSON.parse(result_response);
            let style = document.getElementById('result-style');
            if (style) style.remove();
            style = document.createElement('style');
            style.id = 'result-style';
            style.textContent = result_data.css;
            document.head.appendChild(style);
            app.className = 'result-wrapper';
            app.replaceChildren();
            app.innerHTML = result_data.html;
            let script = document.getElementById('result-script');
            if (script) script.remove();
            script = document.createElement('script');
            script.id = 'result-script';
            script.textContent = result_data.js;
            document.body.appendChild(script);
            app.style.transform = 'translateY(30px)';
            app.offsetHeight;
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '1';
            app.style.transform = 'translateY(0)';
          }, 400);
        };
        window.backToMenu = async function() {
          try {
            const responseStr = await pywebview.api.backToMain();
            const data = JSON.parse(responseStr);
            const app = document.getElementById('app') || document.body;
            const oldStyle = document.getElementById('result-style') || document.getElementById('main-style');
            if (oldStyle) oldStyle.remove();
            const oldScript = document.getElementById('result-script') || document.getElementById('main-script');
            if (oldScript) oldScript.remove();
            if (data.css) {
              const style = document.createElement('style');
              style.id = 'main-style';
              style.textContent = data.css;
              document.head.appendChild(style);
            }
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '0';
            app.style.transform = 'translateY(20px)';
            setTimeout(() => {
              app.replaceChildren();
              app.innerHTML = data.html || '';
              app.className = 'container';
              if (data.js) {
                const script = document.createElement('script');
                script.id = 'main-script';
                script.textContent = data.js;
                document.body.appendChild(script);
              }
              app.style.transform = 'translateY(-20px)';
              app.offsetHeight;
              app.style.opacity = '1';
              app.style.transform = 'translateY(0)';
              if (typeof attachHandlers === 'function') setTimeout(attachHandlers, 50);
            }, 500);
          } catch (e) {
            window.showError('Ошибка при возврате в меню: ' + (e && e.message ? e.message : String(e)));
          }
        };
        window.__task_js__ = (function(){ return `/* task js source placeholder */`; })();
        function attachHandlers(){
          const comp = document.getElementById('computeBtn');
          if (comp) comp.addEventListener('click', window.compute);
          const menu = document.getElementById('toMenuBtn');
          if (menu) menu.addEventListener('click', window.backToMenu);
          const detail = document.getElementById('detail');
          if (detail) detail.focus();
        }
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', attachHandlers);
        } else {
          attachHandlers();
        }
      })();
    </script>
  </body>
</html>
'''

task7_result_txt = r'''
<html>
  <head>
    <style>
      .result-main-container {
        max-width: 800px;
        padding: 40px;
        border-radius: 25px;
        border: 2px solid white;
        background: rgba(0, 0, 0, 0.6);
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.4);
        color: white;
        font-family: Arial, sans-serif;
        margin: 0 auto;
      }
      .result-container {
        text-align: center;
        padding: 20px;
      }
      .result-h2 {
        color: rgb(61, 106, 255);
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 30px;
      }
      .result-box {
        border: 2px solid yellow;
        border-radius: 10px;
        padding: 15px;
        background: rgba(255, 255, 0, 0.1);
        margin: 20px 0;
      }
      .result-box h3 {
        color: rgb(61, 106, 255);
        margin-bottom: 10px;
        font-size: 16px;
        text-transform: uppercase;
      }
      .result-box pre {
        color: white;
        background: none;
        margin: 0;
        font-family: monospace;
        white-space: pre-wrap;
        font-size: 14px;
      }
      .back-section {
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, 0.3);
        text-align: center;
      }
      .back-btn {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(61, 106, 255);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: rgb(61, 106, 255);
        cursor: pointer;
        margin: 10px;
        transition: all 0.2s ease;
      }
      .back-btn:hover {
        background: rgb(61, 106, 255);
        color: white;
        box-shadow: 0 0 20px rgba(0, 142, 236, 0.5);
      }
      .result-wrapper {
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
      }
      body {
        overflow: hidden;
        margin: 0;
      }
    </style>
  </head>
  <body>
    <div class="result-main-container">
      <div class="result-container">
        <h2 class="result-h2">Результат</h2>
        <div class="result-box">
          <h3>Деталь:</h3>
          <pre>{detail}</pre>
        </div>
        <div class="result-box">
          <h3>Количество:</h3>
          <pre>{count}</pre>
        </div>
        <div class="result-box">
          <h3>Общая стоимость:</h3>
          <pre>{total}</pre>
        </div>
        <div class="back-section">
          <button class="back-btn" id="backToInputBtn">Назад</button>
          <button class="back-btn" id="toMenuBtn">В меню</button>
        </div>
      </div>
    </div>
    <script>
      (function(){
        window.backToInput = function() {
          const app = document.getElementById('app');
          app.style.transition = 'all 0.5s ease';
          app.style.opacity = '0';
          app.style.transform = 'translateY(-100%)';
          setTimeout(() => {
            const resultStyle = document.getElementById('result-style');
            if (resultStyle) resultStyle.remove();
            const resultScript = document.getElementById('result-script');
            if (resultScript) resultScript.remove();
            const taskData = window.task7Data;
            if (!taskData) {
              alert('Ошибка: исходное задание не найдено');
              return;
            }
            const taskStyle = document.createElement('style');
            taskStyle.id = 'task7-style';
            taskStyle.textContent = taskData.css || '';
            document.head.appendChild(taskStyle);
            app.className = 'task-container';
            app.innerHTML = taskData.html || '';
            const taskScript = document.createElement('script');
            taskScript.id = 'task7-script';
            taskScript.textContent = taskData.js || '';
            document.body.appendChild(taskScript);
            setTimeout(() => {
              const comp = document.getElementById('computeBtn');
              if (comp && window.compute) comp.addEventListener('click', window.compute);
              const menu = document.getElementById('toMenuBtn');
              if (menu && window.backToMenu) menu.addEventListener('click', window.backToMenu);
              const detail = document.getElementById('detail');
              if (detail) detail.focus();
            }, 100);
            app.style.opacity = '1';
            app.style.transform = 'translateY(0)';
            app.style.transition = '';
          }, 500);
        };
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', function(){
            const b = document.getElementById('backToInputBtn');
            if (b) b.addEventListener('click', window.backToInput);
            const m = document.getElementById('toMenuBtn');
            if (m) m.addEventListener('click', window.backToMenu);
          });
        } else {
          const b = document.getElementById('backToInputBtn');
          if (b) b.addEventListener('click', window.backToInput);
          const m = document.getElementById('toMenuBtn');
          if (m) m.addEventListener('click', window.backToMenu);
        }
        window.backToMenu = async function() {
          try {
            const responseStr = await pywebview.api.backToMain();
            const data = JSON.parse(responseStr);
            const app = document.getElementById('app') || document.body;
            const oldStyle = document.getElementById('result-style') || document.getElementById('main-style');
            if (oldStyle) oldStyle.remove();
            const oldScript = document.getElementById('result-script') || document.getElementById('main-script');
            if (oldScript) oldScript.remove();
            if (data.css) {
              const style = document.createElement('style');
              style.id = 'main-style';
              style.textContent = data.css;
              document.head.appendChild(style);
            }
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '0';
            app.style.transform = 'translateY(20px)';
            setTimeout(() => {
              app.replaceChildren();
              app.innerHTML = data.html || '';
              app.className = 'container';
              if (data.js) {
                const script = document.createElement('script');
                script.id = 'main-script';
                script.textContent = data.js;
                document.body.appendChild(script);
              }
              app.style.transform = 'translateY(-20px)';
              app.offsetHeight;
              app.style.opacity = '1';
              app.style.transform = 'translateY(0)';
              if (typeof attachHandlers === 'function') setTimeout(attachHandlers, 50);
            }, 500);
          } catch (e) {
            window.showError('Ошибка при возврате в меню: ' + (e && e.message ? e.message : String(e)));
          }
        };
      })();
    </script>
  </body>
</html>
'''

task8_txt = r'''
<html>
  <head>
    <style>
      .task-container {
        max-width: 600px;
        max-height: 80vh;
        overflow-y: auto;
        padding: 40px;
        border-radius: 25px;
        border: 2px solid #fff;
        background: rgba(0, 0, 0, .6);
        box-shadow: 0 0 25px rgba(255, 255, 255, .4);
        color: #fff;
        font-family: Arial, sans-serif;
      }
      .task-container::-webkit-scrollbar {
        width: 8px;
      }
      .task-container::-webkit-scrollbar-track {
        background: rgba(0, 0, 0, .3);
        border-top-right-radius: 25px;
        border-bottom-right-radius: 25px;
      }
      .task-container::-webkit-scrollbar-thumb {
        background: rgb(61, 106, 255);
        border-radius: 25px;
        margin: 4px 0;
      }
      .task-container::-webkit-scrollbar-thumb:hover {
        background: rgb(0, 142, 236);
      }
      .task-h2 {
        text-align: center;
        color: rgb(61, 106, 255);
        text-transform: uppercase;
        letter-spacing: 1px;
      }
      .task-label {
        font-weight: 600;
        color: #fff;
      }
      .task-input {
        padding: 10px;
        border-radius: 8px;
        border: 1px solid rgb(61, 106, 255);
        background: rgba(255, 255, 255, .1);
        color: #fff;
        margin: 5px;
        width: 200px;
      }
      .task-input::placeholder {
        color: rgba(255, 255, 255, .7);
      }
      .task-button {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(61, 106, 255);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: #fff;
        overflow: hidden;
        transition: all .2s ease-in;
        cursor: pointer;
        margin: 10px;
      }
      .task-button:hover {
        background: rgb(61, 106, 255);
        box-shadow: 0 0 20px 3px rgba(0, 142, 236, .815);
        transition: all .2s ease-out;
      }
      .back-section {
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, .3);
        text-align: center;
      }
      .error-modal {
        display: none;
        position: fixed;
        z-index: 1000;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, .8);
        backdrop-filter: blur(5px);
        opacity: 0;
        transition: opacity .3s ease;
      }
      .error-content {
        background: linear-gradient(135deg, rgba(0, 0, 0, .95), rgba(20, 20, 40, .95));
        border: 2px solid rgb(255, 61, 61);
        border-radius: 15px;
        margin: 15% auto;
        padding: 30px;
        width: 80%;
        max-width: 400px;
        color: #fff;
        text-align: center;
        box-shadow: 0 0 40px rgba(255, 61, 61, .3), inset 0 0 20px rgba(255, 255, 255, .05);
        animation: errorSlideIn .3s ease-out;
      }
      @keyframes errorSlideIn {
        from {
          transform: translateY(-50px);
          opacity: 0;
        }
        to {
          transform: translateY(0);
          opacity: 1;
        }
      }
      .error-content h3 {
        color: rgb(255, 61, 61);
        margin-bottom: 15px;
        font-size: 24px;
        text-transform: uppercase;
        letter-spacing: 1px;
      }
      .error-content p {
        font-size: 16px;
        margin-bottom: 20px;
        line-height: 1.4;
      }
      .error-close {
        color: rgba(255, 255, 255, .7);
        float: right;
        font-size: 28px;
        font-weight: 700;
        cursor: pointer;
        transition: color .2s ease;
        background: none;
        border: none;
        line-height: 1;
      }
      .error-close:hover {
        color: rgb(255, 61, 61);
      }
      .error-ok {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(255, 61, 61);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: #fff;
        cursor: pointer;
        margin-top: 10px;
        transition: all .2s ease;
      }
      .error-ok:hover {
        background: rgb(255, 61, 61);
        box-shadow: 0 0 20px 3px rgba(255, 0, 0, .5);
      }
    </style>
  </head>
  <body>
    <h2 class="task-h2">Задание 8. Песни</h2>
    <label class="task-label">Сколько песен выбрать?</label>
    <input type="number" id="n" min="1" max="9" class="task-input" placeholder="Введите число"><br><br>
    <button class="task-button" id="genBtn">Генерировать поля</button><br><br>
    <div id="fields"></div><br>
    <button class="task-button" id="computeBtn" style="display:none;">Вычислить</button>
    <div class="back-section">
      <button class="task-button" id="toMenuBtn">Назад к меню</button>
    </div>
    <script>
      (function(){
        window.originalTaskHTML = document.querySelector('.task-container') ? document.querySelector('.task-container').innerHTML : document.getElementById('app').innerHTML || '';
        if (!document.getElementById('task8-style')) {
          const s = document.createElement('style');
          s.id = 'task8-style';
          s.textContent = window.__task_css__ || '';
          document.head.appendChild(s);
        }
        window.closeModal = function(modal) {
          modal.style.opacity = '0';
          setTimeout(() => { modal.remove(); }, 300);
        };
        window.showError = function(message) {
          const modal = document.createElement('div');
          modal.className = 'error-modal';
          modal.innerHTML = `<div class="error-content"><button class="error-close" aria-label="close">&times;</button><h3>Ошибка!</h3><p>${message}</p><button class="error-ok">OK</button></div>`;
          document.body.appendChild(modal);
          modal.style.display = 'block';
          setTimeout(() => { modal.style.opacity = '1'; }, 10);
          const closeSpan = modal.querySelector('.error-close');
          closeSpan.onclick = () => closeModal(modal);
          modal.querySelector('.error-ok').onclick = () => closeModal(modal);
          modal.addEventListener('click', (e) => {
            if (e.target === modal) closeModal(modal);
          });
        };
        window.generateFields = function() {
          const nInput = document.getElementById('n');
          let n = parseInt(nInput.value);
          if (n < 1 || n > 9 || isNaN(n)) {
            window.showError('Введите корректное число песен (1-9)');
            return;
          }
          let fields = '';
          for (let i = 1; i <= n; i++) {
            fields += `<label class="task-label">Название ${i}-й песни: </label><input type="text" id="song${i}" class="task-input" placeholder="Введите название"><br><br>`;
          }
          document.getElementById('fields').innerHTML = fields;
          document.getElementById('computeBtn').style.display = 'block';
          const container = document.querySelector('.task-container') || document.getElementById('app');
          if (container) container.scrollTop = 0;
        };
        window.compute = async function() {
          let n = parseInt(document.getElementById('n').value);
          let songs = [];
          let valid = true;
          for (let i = 1; i <= n; i++) {
            let val = document.getElementById(`song${i}`).value.trim();
            if (!val) {
              window.showError(`Введите название для ${i}-й песни`);
              valid = false;
              break;
            }
            songs.push(val);
          }
          if (!valid) return;
          let data = { n: n, songs: songs };
          const compute_result_str = await pywebview.api.compute_task8(JSON.stringify(data));
          const compute_data = JSON.parse(compute_result_str);
          if (compute_data.error) {
            window.showError(compute_data.error);
            return;
          }
          const styleText = document.getElementById('task8-style') ? document.getElementById('task8-style').textContent : '';
          const scriptText = window.__task_js__ || '';
          const htmlText = window.originalTaskHTML || (document.querySelector('.task-container') ? document.querySelector('.task-container').innerHTML : document.getElementById('app').innerHTML);
          window.task8Data = { css: styleText, html: htmlText, js: scriptText };
          const app = document.getElementById('app');
          app.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
          app.style.opacity = '0';
          app.style.transform = 'translateY(-30px)';
          setTimeout(async () => {
            const result_response = await pywebview.api.get_task8_result_content(JSON.stringify(compute_data));
            const result_data = JSON.parse(result_response);
            let style = document.getElementById('result-style');
            if (style) style.remove();
            style = document.createElement('style');
            style.id = 'result-style';
            style.textContent = result_data.css;
            document.head.appendChild(style);
            app.className = 'result-wrapper';
            app.replaceChildren();
            app.innerHTML = result_data.html;
            let script = document.getElementById('result-script');
            if (script) script.remove();
            script = document.createElement('script');
            script.id = 'result-script';
            script.textContent = result_data.js;
            document.body.appendChild(script);
            app.style.transform = 'translateY(30px)';
            app.offsetHeight;
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '1';
            app.style.transform = 'translateY(0)';
          }, 400);
        };
        window.backToMenu = async function() {
          try {
            const responseStr = await pywebview.api.backToMain();
            const data = JSON.parse(responseStr);
            const app = document.getElementById('app') || document.body;
            const oldStyle = document.getElementById('result-style') || document.getElementById('main-style');
            if (oldStyle) oldStyle.remove();
            const oldScript = document.getElementById('result-script') || document.getElementById('main-script');
            if (oldScript) oldScript.remove();
            if (data.css) {
              const style = document.createElement('style');
              style.id = 'main-style';
              style.textContent = data.css;
              document.head.appendChild(style);
            }
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '0';
            app.style.transform = 'translateY(20px)';
            setTimeout(() => {
              app.replaceChildren();
              app.innerHTML = data.html || '';
              app.className = 'container';
              if (data.js) {
                const script = document.createElement('script');
                script.id = 'main-script';
                script.textContent = data.js;
                document.body.appendChild(script);
              }
              app.style.transform = 'translateY(-20px)';
              app.offsetHeight;
              app.style.opacity = '1';
              app.style.transform = 'translateY(0)';
              if (typeof attachHandlers === 'function') setTimeout(attachHandlers, 50);
            }, 500);
          } catch (e) {
            window.showError('Ошибка при возврате в меню: ' + (e && e.message ? e.message : String(e)));
          }
        };
        window.__task_js__ = (function(){ return `/* task js source placeholder */`; })();
        function attachHandlers(){
          const gen = document.getElementById('genBtn');
          if (gen) gen.addEventListener('click', window.generateFields);
          const comp = document.getElementById('computeBtn');
          if (comp) comp.addEventListener('click', window.compute);
          const menu = document.getElementById('toMenuBtn');
          if (menu) menu.addEventListener('click', window.backToMenu);
          const n = document.getElementById('n');
          if (n) n.focus();
        }
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', attachHandlers);
        } else {
          attachHandlers();
        }
      })();
    </script>
  </body>
</html>
'''

task8_result_txt = r'''
<html>
  <head>
    <style>
      .result-main-container {
        max-width: 800px;
        padding: 40px;
        border-radius: 25px;
        border: 2px solid white;
        background: rgba(0, 0, 0, 0.6);
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.4);
        color: white;
        font-family: Arial, sans-serif;
        margin: 0 auto;
      }
      .result-container {
        text-align: center;
        padding: 20px;
      }
      .result-h2 {
        color: rgb(61, 106, 255);
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 30px;
      }
      .result-box {
        border: 2px solid yellow;
        border-radius: 10px;
        padding: 15px;
        background: rgba(255, 255, 0, 0.1);
        margin: 20px 0;
      }
      .result-box h3 {
        color: rgb(61, 106, 255);
        margin-bottom: 10px;
        font-size: 16px;
        text-transform: uppercase;
      }
      .result-box pre {
        color: white;
        background: none;
        margin: 0;
        font-family: monospace;
        white-space: pre-wrap;
        font-size: 14px;
      }
      .back-section {
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, 0.3);
        text-align: center;
      }
      .back-btn {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(61, 106, 255);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: rgb(61, 106, 255);
        cursor: pointer;
        margin: 10px;
        transition: all 0.2s ease;
      }
      .back-btn:hover {
        background: rgb(61, 106, 255);
        color: white;
        box-shadow: 0 0 20px rgba(0, 142, 236, 0.5);
      }
      .result-wrapper {
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
      }
      body {
        overflow: hidden;
        margin: 0;
      }
    </style>
  </head>
  <body>
    <div class="result-main-container">
      <div class="result-container">
        <h2 class="result-h2">Результат</h2>
        <div class="result-box">
          <h3>Общее время:</h3>
          <pre>{total_time}</pre>
        </div>
        <div class="back-section">
          <button class="back-btn" id="backToInputBtn">Назад</button>
          <button class="back-btn" id="toMenuBtn">В меню</button>
        </div>
      </div>
    </div>
    <script>
      (function(){
        window.backToInput = function() {
          const app = document.getElementById('app');
          app.style.transition = 'all 0.5s ease';
          app.style.opacity = '0';
          app.style.transform = 'translateY(-100%)';
          setTimeout(() => {
            const resultStyle = document.getElementById('result-style');
            if (resultStyle) resultStyle.remove();
            const resultScript = document.getElementById('result-script');
            if (resultScript) resultScript.remove();
            const taskData = window.task8Data;
            if (!taskData) {
              alert('Ошибка: исходное задание не найдено');
              return;
            }
            const taskStyle = document.createElement('style');
            taskStyle.id = 'task8-style';
            taskStyle.textContent = taskData.css || '';
            document.head.appendChild(taskStyle);
            app.className = 'task-container';
            app.innerHTML = taskData.html || '';
            const taskScript = document.createElement('script');
            taskScript.id = 'task8-script';
            taskScript.textContent = taskData.js || '';
            document.body.appendChild(taskScript);
            setTimeout(() => {
              const gen = document.getElementById('genBtn');
              if (gen && window.generateFields) gen.addEventListener('click', window.generateFields);
              const comp = document.getElementById('computeBtn');
              if (comp && window.compute) comp.addEventListener('click', window.compute);
              const menu = document.getElementById('toMenuBtn');
              if (menu && window.backToMenu) menu.addEventListener('click', window.backToMenu);
              const n = document.getElementById('n');
              if (n) n.focus();
            }, 100);
            app.style.opacity = '1';
            app.style.transform = 'translateY(0)';
            app.style.transition = '';
          }, 500);
        };
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', function(){
            const b = document.getElementById('backToInputBtn');
            if (b) b.addEventListener('click', window.backToInput);
            const m = document.getElementById('toMenuBtn');
            if (m) m.addEventListener('click', window.backToMenu);
          });
        } else {
          const b = document.getElementById('backToInputBtn');
          if (b) b.addEventListener('click', window.backToInput);
          const m = document.getElementById('toMenuBtn');
          if (m) m.addEventListener('click', window.backToMenu);
        }
        window.backToMenu = async function() {
          try {
            const responseStr = await pywebview.api.backToMain();
            const data = JSON.parse(responseStr);
            const app = document.getElementById('app') || document.body;
            const oldStyle = document.getElementById('result-style') || document.getElementById('main-style');
            if (oldStyle) oldStyle.remove();
            const oldScript = document.getElementById('result-script') || document.getElementById('main-script');
            if (oldScript) oldScript.remove();
            if (data.css) {
              const style = document.createElement('style');
              style.id = 'main-style';
              style.textContent = data.css;
              document.head.appendChild(style);
            }
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '0';
            app.style.transform = 'translateY(20px)';
            setTimeout(() => {
              app.replaceChildren();
              app.innerHTML = data.html || '';
              app.className = 'container';
              if (data.js) {
                const script = document.createElement('script');
                script.id = 'main-script';
                script.textContent = data.js;
                document.body.appendChild(script);
              }
              app.style.transform = 'translateY(-20px)';
              app.offsetHeight;
              app.style.opacity = '1';
              app.style.transform = 'translateY(0)';
              if (typeof attachHandlers === 'function') setTimeout(attachHandlers, 50);
            }, 500);
          } catch (e) {
            window.showError('Ошибка при возврате в меню: ' + (e && e.message ? e.message : String(e)));
          }
        };
      })();
    </script>
  </body>
</html>
'''

task9_txt = r'''
<html>
  <head>
    <style>
      .task-container {
        max-width: 600px;
        max-height: 80vh;
        overflow-y: auto;
        padding: 40px;
        border-radius: 25px;
        border: 2px solid #fff;
        background: rgba(0, 0, 0, .6);
        box-shadow: 0 0 25px rgba(255, 255, 255, .4);
        color: #fff;
        font-family: Arial, sans-serif;
      }
      .task-container::-webkit-scrollbar {
        width: 8px;
      }
      .task-container::-webkit-scrollbar-track {
        background: rgba(0, 0, 0, .3);
        border-top-right-radius: 25px;
        border-bottom-right-radius: 25px;
      }
      .task-container::-webkit-scrollbar-thumb {
        background: rgb(61, 106, 255);
        border-radius: 25px;
        margin: 4px 0;
      }
      .task-container::-webkit-scrollbar-thumb:hover {
        background: rgb(0, 142, 236);
      }
      .task-h2 {
        text-align: center;
        color: rgb(61, 106, 255);
        text-transform: uppercase;
        letter-spacing: 1px;
      }
      .task-label {
        font-weight: 600;
        color: #fff;
      }
      .task-input {
        padding: 10px;
        border-radius: 8px;
        border: 1px solid rgb(61, 106, 255);
        background: rgba(255, 255, 255, .1);
        color: #fff;
        margin: 5px;
        width: 200px;
      }
      .task-input::placeholder {
        color: rgba(255, 255, 255, .7);
      }
      .task-button {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(61, 106, 255);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: #fff;
        overflow: hidden;
        transition: all .2s ease-in;
        cursor: pointer;
        margin: 10px;
      }
      .task-button:hover {
        background: rgb(61, 106, 255);
        box-shadow: 0 0 20px 3px rgba(0, 142, 236, .815);
        transition: all .2s ease-out;
      }
      .back-section {
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, .3);
        text-align: center;
      }
      .error-modal {
        display: none;
        position: fixed;
        z-index: 1000;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, .8);
        backdrop-filter: blur(5px);
        opacity: 0;
        transition: opacity .3s ease;
      }
      .error-content {
        background: linear-gradient(135deg, rgba(0, 0, 0, .95), rgba(20, 20, 40, .95));
        border: 2px solid rgb(255, 61, 61);
        border-radius: 15px;
        margin: 15% auto;
        padding: 30px;
        width: 80%;
        max-width: 400px;
        color: #fff;
        text-align: center;
        box-shadow: 0 0 40px rgba(255, 61, 61, .3), inset 0 0 20px rgba(255, 255, 255, .05);
        animation: errorSlideIn .3s ease-out;
      }
      @keyframes errorSlideIn {
        from {
          transform: translateY(-50px);
          opacity: 0;
        }
        to {
          transform: translateY(0);
          opacity: 1;
        }
      }
      .error-content h3 {
        color: rgb(255, 61, 61);
        margin-bottom: 15px;
        font-size: 24px;
        text-transform: uppercase;
        letter-spacing: 1px;
      }
      .error-content p {
        font-size: 16px;
        margin-bottom: 20px;
        line-height: 1.4;
      }
      .error-close {
        color: rgba(255, 255, 255, .7);
        float: right;
        font-size: 28px;
        font-weight: 700;
        cursor: pointer;
        transition: color .2s ease;
        background: none;
        border: none;
        line-height: 1;
      }
      .error-close:hover {
        color: rgb(255, 61, 61);
      }
      .error-ok {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(255, 61, 61);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: #fff;
        cursor: pointer;
        margin-top: 10px;
        transition: all .2s ease;
      }
      .error-ok:hover {
        background: rgb(255, 61, 61);
        box-shadow: 0 0 20px 3px rgba(255, 0, 0, .5);
      }
      .list-section {
        margin: 20px 0;
      }
    </style>
  </head>
  <body>
    <h2 class="task-h2">Задание 9. Ролики</h2>
    <div class="list-section">
      <label class="task-label">Количество роликов:</label>
      <input type="number" id="n" min="1" class="task-input" placeholder="Введите число"><br><br>
      <button class="task-button" id="genBtn1">Генерировать поля для роликов</button><br><br>
      <div id="fields1"></div><br>
    </div>
    <div class="list-section">
      <label class="task-label">Количество людей:</label>
      <input type="number" id="k" min="1" class="task-input" placeholder="Введите число"><br><br>
      <button class="task-button" id="genBtn2">Генерировать поля для людей</button><br><br>
      <div id="fields2"></div><br>
    </div>
    <button class="task-button" id="computeBtn" style="display:none;">Вычислить</button>
    <div class="back-section">
      <button class="task-button" id="toMenuBtn">Назад к меню</button>
    </div>
    <script>
      (function(){
        window.originalTaskHTML = document.querySelector('.task-container') ? document.querySelector('.task-container').innerHTML : document.getElementById('app').innerHTML || '';
        if (!document.getElementById('task9-style')) {
          const s = document.createElement('style');
          s.id = 'task9-style';
          s.textContent = window.__task_css__ || '';
          document.head.appendChild(s);
        }
        window.closeModal = function(modal) {
          modal.style.opacity = '0';
          setTimeout(() => { modal.remove(); }, 300);
        };
        window.showError = function(message) {
          const modal = document.createElement('div');
          modal.className = 'error-modal';
          modal.innerHTML = `<div class="error-content"><button class="error-close" aria-label="close">&times;</button><h3>Ошибка!</h3><p>${message}</p><button class="error-ok">OK</button></div>`;
          document.body.appendChild(modal);
          modal.style.display = 'block';
          setTimeout(() => { modal.style.opacity = '1'; }, 10);
          const closeSpan = modal.querySelector('.error-close');
          closeSpan.onclick = () => closeModal(modal);
          modal.querySelector('.error-ok').onclick = () => closeModal(modal);
          modal.addEventListener('click', (e) => {
            if (e.target === modal) closeModal(modal);
          });
        };
        window.generateSkates = function() {
          const nInput = document.getElementById('n');
          let n = parseInt(nInput.value);
          if (n < 1 || isNaN(n)) {
            window.showError('Введите корректное количество роликов (минимум 1)');
            return;
          }
          let fields = '';
          for (let i = 1; i <= n; i++) {
            fields += `<label class="task-label">Размер пары ${i}: </label><input type="number" id="skate${i}" class="task-input" placeholder="Введите размер"><br><br>`;
          }
          document.getElementById('fields1').innerHTML = fields;
          if (document.getElementById('fields2').innerHTML.trim() !== '') {
            document.getElementById('computeBtn').style.display = 'block';
          }
        };
        window.generatePeople = function() {
          const kInput = document.getElementById('k');
          let k = parseInt(kInput.value);
          if (k < 1 || isNaN(k)) {
            window.showError('Введите корректное количество людей (минимум 1)');
            return;
          }
          let fields = '';
          for (let i = 1; i <= k; i++) {
            fields += `<label class="task-label">Размер ноги человека ${i}: </label><input type="number" id="foot${i}" class="task-input" placeholder="Введите размер"><br><br>`;
          }
          document.getElementById('fields2').innerHTML = fields;
          if (document.getElementById('fields1').innerHTML.trim() !== '') {
            document.getElementById('computeBtn').style.display = 'block';
          }
        };
        window.compute = async function() {
          let skates = [];
          let feet = [];
          let valid = true;
          if (document.getElementById('fields1').innerHTML.trim() === '') {
            window.showError('Генерируйте поля для роликов');
            return;
          }
          let n = parseInt(document.getElementById('n').value);
          for (let i = 1; i <= n; i++) {
            let val = parseInt(document.getElementById(`skate${i}`).value);
            if (isNaN(val)) {
              window.showError(`Введите размер для пары ${i}`);
              valid = false;
              break;
            }
            skates.push(val);
          }
          if (!valid) return;
          if (document.getElementById('fields2').innerHTML.trim() === '') {
            window.showError('Генерируйте поля для людей');
            return;
          }
          let k = parseInt(document.getElementById('k').value);
          for (let i = 1; i <= k; i++) {
            let val = parseInt(document.getElementById(`foot${i}`).value);
            if (isNaN(val)) {
              window.showError(`Введите размер для человека ${i}`);
              valid = false;
              break;
            }
            feet.push(val);
          }
          if (!valid) return;
          let data = { skates: skates, feet: feet };
          const compute_result_str = await pywebview.api.compute_task9(JSON.stringify(data));
          const compute_data = JSON.parse(compute_result_str);
          if (compute_data.error) {
            window.showError(compute_data.error);
            return;
          }
          const styleText = document.getElementById('task9-style') ? document.getElementById('task9-style').textContent : '';
          const scriptText = window.__task_js__ || '';
          const htmlText = window.originalTaskHTML || (document.querySelector('.task-container') ? document.querySelector('.task-container').innerHTML : document.getElementById('app').innerHTML);
          window.task9Data = { css: styleText, html: htmlText, js: scriptText };
          const app = document.getElementById('app');
          app.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
          app.style.opacity = '0';
          app.style.transform = 'translateY(-30px)';
          setTimeout(async () => {
            const result_response = await pywebview.api.get_task9_result_content(JSON.stringify(compute_data));
            const result_data = JSON.parse(result_response);
            let style = document.getElementById('result-style');
            if (style) style.remove();
            style = document.createElement('style');
            style.id = 'result-style';
            style.textContent = result_data.css;
            document.head.appendChild(style);
            app.className = 'result-wrapper';
            app.replaceChildren();
            app.innerHTML = result_data.html;
            let script = document.getElementById('result-script');
            if (script) script.remove();
            script = document.createElement('script');
            script.id = 'result-script';
            script.textContent = result_data.js;
            document.body.appendChild(script);
            app.style.transform = 'translateY(30px)';
            app.offsetHeight;
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '1';
            app.style.transform = 'translateY(0)';
          }, 400);
        };
        window.backToMenu = async function() {
          try {
            const responseStr = await pywebview.api.backToMain();
            const data = JSON.parse(responseStr);
            const app = document.getElementById('app') || document.body;
            const oldStyle = document.getElementById('result-style') || document.getElementById('main-style');
            if (oldStyle) oldStyle.remove();
            const oldScript = document.getElementById('result-script') || document.getElementById('main-script');
            if (oldScript) oldScript.remove();
            if (data.css) {
              const style = document.createElement('style');
              style.id = 'main-style';
              style.textContent = data.css;
              document.head.appendChild(style);
            }
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '0';
            app.style.transform = 'translateY(20px)';
            setTimeout(() => {
              app.replaceChildren();
              app.innerHTML = data.html || '';
              app.className = 'container';
              if (data.js) {
                const script = document.createElement('script');
                script.id = 'main-script';
                script.textContent = data.js;
                document.body.appendChild(script);
              }
              app.style.transform = 'translateY(-20px)';
              app.offsetHeight;
              app.style.opacity = '1';
              app.style.transform = 'translateY(0)';
              if (typeof attachHandlers === 'function') setTimeout(attachHandlers, 50);
            }, 500);
          } catch (e) {
            window.showError('Ошибка при возврате в меню: ' + (e && e.message ? e.message : String(e)));
          }
        };
        window.__task_js__ = (function(){ return `/* task js source placeholder */`; })();
        function attachHandlers(){
          const gen1 = document.getElementById('genBtn1');
          if (gen1) gen1.addEventListener('click', window.generateSkates);
          const gen2 = document.getElementById('genBtn2');
          if (gen2) gen2.addEventListener('click', window.generatePeople);
          const comp = document.getElementById('computeBtn');
          if (comp) comp.addEventListener('click', window.compute);
          const menu = document.getElementById('toMenuBtn');
          if (menu) menu.addEventListener('click', window.backToMenu);
          const n = document.getElementById('n');
          if (n) n.focus();
        }
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', attachHandlers);
        } else {
          attachHandlers();
        }
      })();
    </script>
  </body>
</html>
'''

task9_result_txt = r'''
<html>
  <head>
    <style>
      .result-main-container {
        max-width: 800px;
        padding: 40px;
        border-radius: 25px;
        border: 2px solid white;
        background: rgba(0, 0, 0, 0.6);
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.4);
        color: white;
        font-family: Arial, sans-serif;
        margin: 0 auto;
      }
      .result-container {
        text-align: center;
        padding: 20px;
      }
      .result-h2 {
        color: rgb(61, 106, 255);
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 30px;
      }
      .result-box {
        border: 2px solid yellow;
        border-radius: 10px;
        padding: 15px;
        background: rgba(255, 255, 0, 0.1);
        margin: 20px 0;
      }
      .result-box h3 {
        color: rgb(61, 106, 255);
        margin-bottom: 10px;
        font-size: 16px;
        text-transform: uppercase;
      }
      .result-box pre {
        color: white;
        background: none;
        margin: 0;
        font-family: monospace;
        white-space: pre-wrap;
        font-size: 14px;
      }
      .back-section {
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, 0.3);
        text-align: center;
      }
      .back-btn {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(61, 106, 255);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: rgb(61, 106, 255);
        cursor: pointer;
        margin: 10px;
        transition: all 0.2s ease;
      }
      .back-btn:hover {
        background: rgb(61, 106, 255);
        color: white;
        box-shadow: 0 0 20px rgba(0, 142, 236, 0.5);
      }
      .result-wrapper {
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
      }
      body {
        overflow: hidden;
        margin: 0;
      }
    </style>
  </head>
  <body>
    <div class="result-main-container">
      <div class="result-container">
        <h2 class="result-h2">Результат</h2>
        <div class="result-box">
          <h3>Наибольшее количество людей:</h3>
          <pre>{max_people}</pre>
        </div>
        <div class="back-section">
          <button class="back-btn" id="backToInputBtn">Назад</button>
          <button class="back-btn" id="toMenuBtn">В меню</button>
        </div>
      </div>
    </div>
    <script>
      (function(){
        window.backToInput = function() {
          const app = document.getElementById('app');
          app.style.transition = 'all 0.5s ease';
          app.style.opacity = '0';
          app.style.transform = 'translateY(-100%)';
          setTimeout(() => {
            const resultStyle = document.getElementById('result-style');
            if (resultStyle) resultStyle.remove();
            const resultScript = document.getElementById('result-script');
            if (resultScript) resultScript.remove();
            const taskData = window.task9Data;
            if (!taskData) {
              alert('Ошибка: исходное задание не найдено');
              return;
            }
            const taskStyle = document.createElement('style');
            taskStyle.id = 'task9-style';
            taskStyle.textContent = taskData.css || '';
            document.head.appendChild(taskStyle);
            app.className = 'task-container';
            app.innerHTML = taskData.html || '';
            const taskScript = document.createElement('script');
            taskScript.id = 'task9-script';
            taskScript.textContent = taskData.js || '';
            document.body.appendChild(taskScript);
            setTimeout(() => {
              const gen1 = document.getElementById('genBtn1');
              if (gen1 && window.generateSkates) gen1.addEventListener('click', window.generateSkates);
              const gen2 = document.getElementById('genBtn2');
              if (gen2 && window.generatePeople) gen2.addEventListener('click', window.generatePeople);
              const comp = document.getElementById('computeBtn');
              if (comp && window.compute) comp.addEventListener('click', window.compute);
              const menu = document.getElementById('toMenuBtn');
              if (menu && window.backToMenu) menu.addEventListener('click', window.backToMenu);
              const n = document.getElementById('n');
              if (n) n.focus();
            }, 100);
            app.style.opacity = '1';
            app.style.transform = 'translateY(0)';
            app.style.transition = '';
          }, 500);
        };
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', function(){
            const b = document.getElementById('backToInputBtn');
            if (b) b.addEventListener('click', window.backToInput);
            const m = document.getElementById('toMenuBtn');
            if (m) m.addEventListener('click', window.backToMenu);
          });
        } else {
          const b = document.getElementById('backToInputBtn');
          if (b) b.addEventListener('click', window.backToInput);
          const m = document.getElementById('toMenuBtn');
          if (m) m.addEventListener('click', window.backToMenu);
        }
        window.backToMenu = async function() {
          try {
            const responseStr = await pywebview.api.backToMain();
            const data = JSON.parse(responseStr);
            const app = document.getElementById('app') || document.body;
            const oldStyle = document.getElementById('result-style') || document.getElementById('main-style');
            if (oldStyle) oldStyle.remove();
            const oldScript = document.getElementById('result-script') || document.getElementById('main-script');
            if (oldScript) oldScript.remove();
            if (data.css) {
              const style = document.createElement('style');
              style.id = 'main-style';
              style.textContent = data.css;
              document.head.appendChild(style);
            }
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '0';
            app.style.transform = 'translateY(20px)';
            setTimeout(() => {
              app.replaceChildren();
              app.innerHTML = data.html || '';
              app.className = 'container';
              if (data.js) {
                const script = document.createElement('script');
                script.id = 'main-script';
                script.textContent = data.js;
                document.body.appendChild(script);
              }
              app.style.transform = 'translateY(-20px)';
              app.offsetHeight;
              app.style.opacity = '1';
              app.style.transform = 'translateY(0)';
              if (typeof attachHandlers === 'function') setTimeout(attachHandlers, 50);
            }, 500);
          } catch (e) {
            window.showError('Ошибка при возврате в меню: ' + (e && e.message ? e.message : String(e)));
          }
        };
      })();
    </script>
  </body>
</html>
'''

task10_txt = r'''
<html>
  <head>
    <style>
      .task-container {
        max-width: 600px;
        max-height: 80vh;
        overflow-y: auto;
        padding: 40px;
        border-radius: 25px;
        border: 2px solid #fff;
        background: rgba(0, 0, 0, .6);
        box-shadow: 0 0 25px rgba(255, 255, 255, .4);
        color: #fff;
        font-family: Arial, sans-serif;
      }
      .task-container::-webkit-scrollbar {
        width: 8px;
      }
      .task-container::-webkit-scrollbar-track {
        background: rgba(0, 0, 0, .3);
        border-top-right-radius: 25px;
        border-bottom-right-radius: 25px;
      }
      .task-container::-webkit-scrollbar-thumb {
        background: rgb(61, 106, 255);
        border-radius: 25px;
        margin: 4px 0;
      }
      .task-container::-webkit-scrollbar-thumb:hover {
        background: rgb(0, 142, 236);
      }
      .task-h2 {
        text-align: center;
        color: rgb(61, 106, 255);
        text-transform: uppercase;
        letter-spacing: 1px;
      }
      .task-label {
        font-weight: 600;
        color: #fff;
      }
      .task-input {
        padding: 10px;
        border-radius: 8px;
        border: 1px solid rgb(61, 106, 255);
        background: rgba(255, 255, 255, .1);
        color: #fff;
        margin: 5px;
        width: 200px;
      }
      .task-input::placeholder {
        color: rgba(255, 255, 255, .7);
      }
      .task-button {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(61, 106, 255);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: #fff;
        overflow: hidden;
        transition: all .2s ease-in;
        cursor: pointer;
        margin: 10px;
      }
      .task-button:hover {
        background: rgb(61, 106, 255);
        box-shadow: 0 0 20px 3px rgba(0, 142, 236, .815);
        transition: all .2s ease-out;
      }
      .back-section {
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, .3);
        text-align: center;
      }
      .error-modal {
        display: none;
        position: fixed;
        z-index: 1000;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, .8);
        backdrop-filter: blur(5px);
        opacity: 0;
        transition: opacity .3s ease;
      }
      .error-content {
        background: linear-gradient(135deg, rgba(0, 0, 0, .95), rgba(20, 20, 40, .95));
        border: 2px solid rgb(255, 61, 61);
        border-radius: 15px;
        margin: 15% auto;
        padding: 30px;
        width: 80%;
        max-width: 400px;
        color: #fff;
        text-align: center;
        box-shadow: 0 0 40px rgba(255, 61, 61, .3), inset 0 0 20px rgba(255, 255, 255, .05);
        animation: errorSlideIn .3s ease-out;
      }
      @keyframes errorSlideIn {
        from {
          transform: translateY(-50px);
          opacity: 0;
        }
        to {
          transform: translateY(0);
          opacity: 1;
        }
      }
      .error-content h3 {
        color: rgb(255, 61, 61);
        margin-bottom: 15px;
        font-size: 24px;
        text-transform: uppercase;
        letter-spacing: 1px;
      }
      .error-content p {
        font-size: 16px;
        margin-bottom: 20px;
        line-height: 1.4;
      }
      .error-close {
        color: rgba(255, 255, 255, .7);
        float: right;
        font-size: 28px;
        font-weight: 700;
        cursor: pointer;
        transition: color .2s ease;
        background: none;
        border: none;
        line-height: 1;
      }
      .error-close:hover {
        color: rgb(255, 61, 61);
      }
      .error-ok {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(255, 61, 61);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: #fff;
        cursor: pointer;
        margin-top: 10px;
        transition: all .2s ease;
      }
      .error-ok:hover {
        background: rgb(255, 61, 61);
        box-shadow: 0 0 20px 3px rgba(255, 0, 0, .5);
      }
    </style>
  </head>
  <body>
    <h2 class="task-h2">Задание 10. Считалка</h2>
    <label class="task-label">Количество человек:</label>
    <input type="number" id="n" min="1" class="task-input" placeholder="Введите N"><br><br>
    <label class="task-label">Какое число в считалке?</label>
    <input type="number" id="k" min="1" class="task-input" placeholder="Введите K"><br><br>
    <button class="task-button" id="computeBtn">Запустить</button>
    <div class="back-section">
      <button class="task-button" id="toMenuBtn">Назад к меню</button>
    </div>
    <script>
      (function(){
        window.originalTaskHTML = document.querySelector('.task-container') ? document.querySelector('.task-container').innerHTML : document.getElementById('app').innerHTML || '';
        if (!document.getElementById('task10-style')) {
          const s = document.createElement('style');
          s.id = 'task10-style';
          s.textContent = window.__task_css__ || '';
          document.head.appendChild(s);
        }
        window.closeModal = function(modal) {
          modal.style.opacity = '0';
          setTimeout(() => { modal.remove(); }, 300);
        };
        window.showError = function(message) {
          const modal = document.createElement('div');
          modal.className = 'error-modal';
          modal.innerHTML = `<div class="error-content"><button class="error-close" aria-label="close">&times;</button><h3>Ошибка!</h3><p>${message}</p><button class="error-ok">OK</button></div>`;
          document.body.appendChild(modal);
          modal.style.display = 'block';
          setTimeout(() => { modal.style.opacity = '1'; }, 10);
          const closeSpan = modal.querySelector('.error-close');
          closeSpan.onclick = () => closeModal(modal);
          modal.querySelector('.error-ok').onclick = () => closeModal(modal);
          modal.addEventListener('click', (e) => {
            if (e.target === modal) closeModal(modal);
          });
        };
        window.compute = async function() {
          let n = parseInt(document.getElementById('n').value);
          let k = parseInt(document.getElementById('k').value);
          if (isNaN(n) || n < 1) {
            window.showError('Введите корректное N (минимум 1)');
            return;
          }
          if (isNaN(k) || k < 1) {
            window.showError('Введите корректное K (минимум 1)');
            return;
          }
          let data = { n: n, k: k };
          const compute_result_str = await pywebview.api.compute_task10(JSON.stringify(data));
          const compute_data = JSON.parse(compute_result_str);
          if (compute_data.error) {
            window.showError(compute_data.error);
            return;
          }
          const styleText = document.getElementById('task10-style') ? document.getElementById('task10-style').textContent : '';
          const scriptText = window.__task_js__ || '';
          const htmlText = window.originalTaskHTML || (document.querySelector('.task-container') ? document.querySelector('.task-container').innerHTML : document.getElementById('app').innerHTML);
          window.task10Data = { css: styleText, html: htmlText, js: scriptText };
          const app = document.getElementById('app');
          app.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
          app.style.opacity = '0';
          app.style.transform = 'translateY(-30px)';
          setTimeout(async () => {
            const result_response = await pywebview.api.get_task10_result_content(JSON.stringify(compute_data));
            const result_data = JSON.parse(result_response);
            let style = document.getElementById('result-style');
            if (style) style.remove();
            style = document.createElement('style');
            style.id = 'result-style';
            style.textContent = result_data.css;
            document.head.appendChild(style);
            app.className = 'result-wrapper';
            app.replaceChildren();
            app.innerHTML = result_data.html;
            let script = document.getElementById('result-script');
            if (script) script.remove();
            script = document.createElement('script');
            script.id = 'result-script';
            script.textContent = result_data.js;
            document.body.appendChild(script);
            app.style.transform = 'translateY(30px)';
            app.offsetHeight;
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '1';
            app.style.transform = 'translateY(0)';
          }, 400);
        };
        window.backToMenu = async function() {
          try {
            const responseStr = await pywebview.api.backToMain();
            const data = JSON.parse(responseStr);
            const app = document.getElementById('app') || document.body;
            const oldStyle = document.getElementById('result-style') || document.getElementById('main-style');
            if (oldStyle) oldStyle.remove();
            const oldScript = document.getElementById('result-script') || document.getElementById('main-script');
            if (oldScript) oldScript.remove();
            if (data.css) {
              const style = document.createElement('style');
              style.id = 'main-style';
              style.textContent = data.css;
              document.head.appendChild(style);
            }
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '0';
            app.style.transform = 'translateY(20px)';
            setTimeout(() => {
              app.replaceChildren();
              app.innerHTML = data.html || '';
              app.className = 'container';
              if (data.js) {
                const script = document.createElement('script');
                script.id = 'main-script';
                script.textContent = data.js;
                document.body.appendChild(script);
              }
              app.style.transform = 'translateY(-20px)';
              app.offsetHeight;
              app.style.opacity = '1';
              app.style.transform = 'translateY(0)';
              if (typeof attachHandlers === 'function') setTimeout(attachHandlers, 50);
            }, 500);
          } catch (e) {
            window.showError('Ошибка при возврате в меню: ' + (e && e.message ? e.message : String(e)));
          }
        };
        window.__task_js__ = (function(){ return `/* task js source placeholder */`; })();
        function attachHandlers(){
          const comp = document.getElementById('computeBtn');
          if (comp) comp.addEventListener('click', window.compute);
          const menu = document.getElementById('toMenuBtn');
          if (menu) menu.addEventListener('click', window.backToMenu);
          const n = document.getElementById('n');
          if (n) n.focus();
        }
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', attachHandlers);
        } else {
          attachHandlers();
        }
      })();
    </script>
  </body>
</html>
'''

task10_result_txt = r'''
<html>
  <head>
    <style>
      .result-main-container {
        max-width: 800px;
        padding: 40px;
        border-radius: 25px;
        border: 2px solid white;
        background: rgba(0, 0, 0, 0.6);
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.4);
        color: white;
        font-family: Arial, sans-serif;
        margin: 0 auto;
      }
      .result-container {
        text-align: center;
        padding: 20px;
      }
      .result-h2 {
        color: rgb(61, 106, 255);
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 30px;
      }
      .result-box {
        border: 2px solid yellow;
        border-radius: 10px;
        padding: 15px;
        background: rgba(255, 255, 0, 0.1);
        margin: 20px 0;
        text-align: left;
      }
      .result-box pre {
        color: white;
        background: none;
        margin: 0;
        font-family: monospace;
        white-space: pre-wrap;
        font-size: 14px;
      }
      .back-section {
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, 0.3);
        text-align: center;
      }
      .back-btn {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(61, 106, 255);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: rgb(61, 106, 255);
        cursor: pointer;
        margin: 10px;
        transition: all 0.2s ease;
      }
      .back-btn:hover {
        background: rgb(61, 106, 255);
        color: white;
        box-shadow: 0 0 20px rgba(0, 142, 236, 0.5);
      }
      .result-wrapper {
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
      }
      body {
        overflow: hidden;
        margin: 0;
      }
    </style>
  </head>
  <body>
    <div class="result-main-container">
      <div class="result-container">
        <h2 class="result-h2">Результат</h2>
        <div class="result-box">
          <pre>{simulation}</pre>
        </div>
        <div class="back-section">
          <button class="back-btn" id="backToInputBtn">Назад</button>
          <button class="back-btn" id="toMenuBtn">В меню</button>
        </div>
      </div>
    </div>
    <script>
      (function(){
        window.backToInput = function() {
          const app = document.getElementById('app');
          app.style.transition = 'all 0.5s ease';
          app.style.opacity = '0';
          app.style.transform = 'translateY(-100%)';
          setTimeout(() => {
            const resultStyle = document.getElementById('result-style');
            if (resultStyle) resultStyle.remove();
            const resultScript = document.getElementById('result-script');
            if (resultScript) resultScript.remove();
            const taskData = window.task10Data;
            if (!taskData) {
              alert('Ошибка: исходное задание не найдено');
              return;
            }
            const taskStyle = document.createElement('style');
            taskStyle.id = 'task10-style';
            taskStyle.textContent = taskData.css || '';
            document.head.appendChild(taskStyle);
            app.className = 'task-container';
            app.innerHTML = taskData.html || '';
            const taskScript = document.createElement('script');
            taskScript.id = 'task10-script';
            taskScript.textContent = taskData.js || '';
            document.body.appendChild(taskScript);
            setTimeout(() => {
              const comp = document.getElementById('computeBtn');
              if (comp && window.compute) comp.addEventListener('click', window.compute);
              const menu = document.getElementById('toMenuBtn');
              if (menu && window.backToMenu) menu.addEventListener('click', window.backToMenu);
              const n = document.getElementById('n');
              if (n) n.focus();
            }, 100);
            app.style.opacity = '1';
            app.style.transform = 'translateY(0)';
            app.style.transition = '';
          }, 500);
        };
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', function(){
            const b = document.getElementById('backToInputBtn');
            if (b) b.addEventListener('click', window.backToInput);
            const m = document.getElementById('toMenuBtn');
            if (m) m.addEventListener('click', window.backToMenu);
          });
        } else {
          const b = document.getElementById('backToInputBtn');
          if (b) b.addEventListener('click', window.backToInput);
          const m = document.getElementById('toMenuBtn');
          if (m) m.addEventListener('click', window.backToMenu);
        }
        window.backToMenu = async function() {
          try {
            const responseStr = await pywebview.api.backToMain();
            const data = JSON.parse(responseStr);
            const app = document.getElementById('app') || document.body;
            const oldStyle = document.getElementById('result-style') || document.getElementById('main-style');
            if (oldStyle) oldStyle.remove();
            const oldScript = document.getElementById('result-script') || document.getElementById('main-script');
            if (oldScript) oldScript.remove();
            if (data.css) {
              const style = document.createElement('style');
              style.id = 'main-style';
              style.textContent = data.css;
              document.head.appendChild(style);
            }
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '0';
            app.style.transform = 'translateY(20px)';
            setTimeout(() => {
              app.replaceChildren();
              app.innerHTML = data.html || '';
              app.className = 'container';
              if (data.js) {
                const script = document.createElement('script');
                script.id = 'main-script';
                script.textContent = data.js;
                document.body.appendChild(script);
              }
              app.style.transform = 'translateY(-20px)';
              app.offsetHeight;
              app.style.opacity = '1';
              app.style.transform = 'translateY(0)';
              if (typeof attachHandlers === 'function') setTimeout(attachHandlers, 50);
            }, 500);
          } catch (e) {
            window.showError('Ошибка при возврате в меню: ' + (e && e.message ? e.message : String(e)));
          }
        };
      })();
    </script>
  </body>
</html>
'''

task11_txt = r'''
<html>
  <head>
    <style>
      .task-container {
        max-width: 600px;
        max-height: 80vh;
        overflow-y: auto;
        padding: 40px;
        border-radius: 25px;
        border: 2px solid #fff;
        background: rgba(0, 0, 0, .6);
        box-shadow: 0 0 25px rgba(255, 255, 255, .4);
        color: #fff;
        font-family: Arial, sans-serif;
      }
      .task-container::-webkit-scrollbar {
        width: 8px;
      }
      .task-container::-webkit-scrollbar-track {
        background: rgba(0, 0, 0, .3);
        border-top-right-radius: 25px;
        border-bottom-right-radius: 25px;
      }
      .task-container::-webkit-scrollbar-thumb {
        background: rgb(61, 106, 255);
        border-radius: 25px;
        margin: 4px 0;
      }
      .task-container::-webkit-scrollbar-thumb:hover {
        background: rgb(0, 142, 236);
      }
      .task-h2 {
        text-align: center;
        color: rgb(61, 106, 255);
        text-transform: uppercase;
        letter-spacing: 1px;
      }
      .task-label {
        font-weight: 600;
        color: #fff;
      }
      .task-input {
        padding: 10px;
        border-radius: 8px;
        border: 1px solid rgb(61, 106, 255);
        background: rgba(255, 255, 255, .1);
        color: #fff;
        margin: 5px;
        width: 200px;
      }
      .task-input::placeholder {
        color: rgba(255, 255, 255, .7);
      }
      .task-button {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(61, 106, 255);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: #fff;
        overflow: hidden;
        transition: all .2s ease-in;
        cursor: pointer;
        margin: 10px;
      }
      .task-button:hover {
        background: rgb(61, 106, 255);
        box-shadow: 0 0 20px 3px rgba(0, 142, 236, .815);
        transition: all .2s ease-out;
      }
      .back-section {
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, .3);
        text-align: center;
      }
      .error-modal {
        display: none;
        position: fixed;
        z-index: 1000;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, .8);
        backdrop-filter: blur(5px);
        opacity: 0;
        transition: opacity .3s ease;
      }
      .error-content {
        background: linear-gradient(135deg, rgba(0, 0, 0, .95), rgba(20, 20, 40, .95));
        border: 2px solid rgb(255, 61, 61);
        border-radius: 15px;
        margin: 15% auto;
        padding: 30px;
        width: 80%;
        max-width: 400px;
        color: #fff;
        text-align: center;
        box-shadow: 0 0 40px rgba(255, 61, 61, .3), inset 0 0 20px rgba(255, 255, 255, .05);
        animation: errorSlideIn .3s ease-out;
      }
      @keyframes errorSlideIn {
        from {
          transform: translateY(-50px);
          opacity: 0;
        }
        to {
          transform: translateY(0);
          opacity: 1;
        }
      }
      .error-content h3 {
        color: rgb(255, 61, 61);
        margin-bottom: 15px;
        font-size: 24px;
        text-transform: uppercase;
        letter-spacing: 1px;
      }
      .error-content p {
        font-size: 16px;
        margin-bottom: 20px;
        line-height: 1.4;
      }
      .error-close {
        color: rgba(255, 255, 255, .7);
        float: right;
        font-size: 28px;
        font-weight: 700;
        cursor: pointer;
        transition: color .2s ease;
        background: none;
        border: none;
        line-height: 1;
      }
      .error-close:hover {
        color: rgb(255, 61, 61);
      }
      .error-ok {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(255, 61, 61);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: #fff;
        cursor: pointer;
        margin-top: 10px;
        transition: all .2s ease;
      }
      .error-ok:hover {
        background: rgb(255, 61, 61);
        box-shadow: 0 0 20px 3px rgba(255, 0, 0, .5);
      }
    </style>
  </head>
  <body>
    <h2 class="task-h2">Задание 11. Симметричная последовательность</h2>
    <label class="task-label">Количество чисел:</label>
    <input type="number" id="n" min="1" class="task-input" placeholder="Введите число"><br><br>
    <button class="task-button" id="genBtn">Генерировать поля</button><br><br>
    <div id="fields"></div><br>
    <button class="task-button" id="computeBtn" style="display:none;">Вычислить</button>
    <div class="back-section">
      <button class="task-button" id="toMenuBtn">Назад к меню</button>
    </div>
    <script>
      (function(){
        window.originalTaskHTML = document.querySelector('.task-container') ? document.querySelector('.task-container').innerHTML : document.getElementById('app').innerHTML || '';
        if (!document.getElementById('task11-style')) {
          const s = document.createElement('style');
          s.id = 'task11-style';
          s.textContent = window.__task_css__ || '';
          document.head.appendChild(s);
        }
        window.closeModal = function(modal) {
          modal.style.opacity = '0';
          setTimeout(() => { modal.remove(); }, 300);
        };
        window.showError = function(message) {
          const modal = document.createElement('div');
          modal.className = 'error-modal';
          modal.innerHTML = `<div class="error-content"><button class="error-close" aria-label="close">&times;</button><h3>Ошибка!</h3><p>${message}</p><button class="error-ok">OK</button></div>`;
          document.body.appendChild(modal);
          modal.style.display = 'block';
          setTimeout(() => { modal.style.opacity = '1'; }, 10);
          const closeSpan = modal.querySelector('.error-close');
          closeSpan.onclick = () => closeModal(modal);
          modal.querySelector('.error-ok').onclick = () => closeModal(modal);
          modal.addEventListener('click', (e) => {
            if (e.target === modal) closeModal(modal);
          });
        };
        window.generateFields = function() {
          const nInput = document.getElementById('n');
          let n = parseInt(nInput.value);
          if (n < 1 || isNaN(n)) {
            window.showError('Введите корректное число (минимум 1)');
            return;
          }
          let fields = '';
          for (let i = 1; i <= n; i++) {
            fields += `<label class="task-label">Число ${i}: </label><input type="number" id="num${i}" class="task-input" placeholder="Введите число"><br><br>`;
          }
          document.getElementById('fields').innerHTML = fields;
          document.getElementById('computeBtn').style.display = 'block';
          const container = document.querySelector('.task-container') || document.getElementById('app');
          if (container) container.scrollTop = 0;
        };
        window.compute = async function() {
          let n = parseInt(document.getElementById('n').value);
          let sequence = [];
          let valid = true;
          for (let i = 1; i <= n; i++) {
            let val = parseInt(document.getElementById(`num${i}`).value);
            if (isNaN(val)) {
              window.showError(`Введите корректное значение для числа ${i}`);
              valid = false;
              break;
            }
            sequence.push(val);
          }
          if (!valid) return;
          let data = { sequence: sequence };
          const compute_result_str = await pywebview.api.compute_task11(JSON.stringify(data));
          const compute_data = JSON.parse(compute_result_str);
          if (compute_data.error) {
            window.showError(compute_data.error);
            return;
          }
          const styleText = document.getElementById('task11-style') ? document.getElementById('task11-style').textContent : '';
          const scriptText = window.__task_js__ || '';
          const htmlText = window.originalTaskHTML || (document.querySelector('.task-container') ? document.querySelector('.task-container').innerHTML : document.getElementById('app').innerHTML);
          window.task11Data = { css: styleText, html: htmlText, js: scriptText };
          const app = document.getElementById('app');
          app.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
          app.style.opacity = '0';
          app.style.transform = 'translateY(-30px)';
          setTimeout(async () => {
            const result_response = await pywebview.api.get_task11_result_content(JSON.stringify(compute_data));
            const result_data = JSON.parse(result_response);
            let style = document.getElementById('result-style');
            if (style) style.remove();
            style = document.createElement('style');
            style.id = 'result-style';
            style.textContent = result_data.css;
            document.head.appendChild(style);
            app.className = 'result-wrapper';
            app.replaceChildren();
            app.innerHTML = result_data.html;
            let script = document.getElementById('result-script');
            if (script) script.remove();
            script = document.createElement('script');
            script.id = 'result-script';
            script.textContent = result_data.js;
            document.body.appendChild(script);
            app.style.transform = 'translateY(30px)';
            app.offsetHeight;
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '1';
            app.style.transform = 'translateY(0)';
          }, 400);
        };
        window.backToMenu = async function() {
          try {
            const responseStr = await pywebview.api.backToMain();
            const data = JSON.parse(responseStr);
            const app = document.getElementById('app') || document.body;
            const oldStyle = document.getElementById('result-style') || document.getElementById('main-style');
            if (oldStyle) oldStyle.remove();
            const oldScript = document.getElementById('result-script') || document.getElementById('main-script');
            if (oldScript) oldScript.remove();
            if (data.css) {
              const style = document.createElement('style');
              style.id = 'main-style';
              style.textContent = data.css;
              document.head.appendChild(style);
            }
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '0';
            app.style.transform = 'translateY(20px)';
            setTimeout(() => {
              app.replaceChildren();
              app.innerHTML = data.html || '';
              app.className = 'container';
              if (data.js) {
                const script = document.createElement('script');
                script.id = 'main-script';
                script.textContent = data.js;
                document.body.appendChild(script);
              }
              app.style.transform = 'translateY(-20px)';
              app.offsetHeight;
              app.style.opacity = '1';
              app.style.transform = 'translateY(0)';
              if (typeof attachHandlers === 'function') setTimeout(attachHandlers, 50);
            }, 500);
          } catch (e) {
            window.showError('Ошибка при возврате в меню: ' + (e && e.message ? e.message : String(e)));
          }
        };
        window.__task_js__ = (function(){ return `/* task js source placeholder */`; })();
        function attachHandlers(){
          const gen = document.getElementById('genBtn');
          if (gen) gen.addEventListener('click', window.generateFields);
          const comp = document.getElementById('computeBtn');
          if (comp) comp.addEventListener('click', window.compute);
          const menu = document.getElementById('toMenuBtn');
          if (menu) menu.addEventListener('click', window.backToMenu);
          const n = document.getElementById('n');
          if (n) n.focus();
        }
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', attachHandlers);
        } else {
          attachHandlers();
        }
      })();
    </script>
  </body>
</html>
'''

task11_result_txt = r'''
<html>
  <head>
    <style>
      .result-main-container {
        max-width: 800px;
        padding: 40px;
        border-radius: 25px;
        border: 2px solid white;
        background: rgba(0, 0, 0, 0.6);
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.4);
        color: white;
        font-family: Arial, sans-serif;
        margin: 0 auto;
      }
      .result-container {
        text-align: center;
        padding: 20px;
      }
      .result-h2 {
        color: rgb(61, 106, 255);
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 30px;
      }
      .result-box {
        border: 2px solid yellow;
        border-radius: 10px;
        padding: 15px;
        background: rgba(255, 255, 0, 0.1);
        margin: 20px 0;
      }
      .result-box h3 {
        color: rgb(61, 106, 255);
        margin-bottom: 10px;
        font-size: 16px;
        text-transform: uppercase;
      }
      .result-box pre {
        color: white;
        background: none;
        margin: 0;
        font-family: monospace;
        white-space: pre-wrap;
        font-size: 14px;
      }
      .back-section {
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, 0.3);
        text-align: center;
      }
      .back-btn {
        padding: 12px 24px;
        border-radius: 12px;
        border: 1px solid rgb(61, 106, 255);
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 1px;
        background: transparent;
        color: rgb(61, 106, 255);
        cursor: pointer;
        margin: 10px;
        transition: all 0.2s ease;
      }
      .back-btn:hover {
        background: rgb(61, 106, 255);
        color: white;
        box-shadow: 0 0 20px rgba(0, 142, 236, 0.5);
      }
      .result-wrapper {
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
      }
      body {
        overflow: hidden;
        margin: 0;
      }
    </style>
  </head>
  <body>
    <div class="result-main-container">
      <div class="result-container">
        <h2 class="result-h2">Результат</h2>
        <div class="result-box">
          <h3>Последовательность:</h3>
          <pre>[ {sequence} ]</pre>
        </div>
        <div class="result-box">
          <h3>Нужно приписать чисел:</h3>
          <pre>{count}</pre>
        </div>
        <div class="result-box">
          <h3>Сами числа:</h3>
          <pre>[ {append_list} ]</pre>
        </div>
        <div class="back-section">
          <button class="back-btn" id="backToInputBtn">Назад</button>
          <button class="back-btn" id="toMenuBtn">В меню</button>
        </div>
      </div>
    </div>
    <script>
      (function(){
        window.backToInput = function() {
          const app = document.getElementById('app');
          app.style.transition = 'all 0.5s ease';
          app.style.opacity = '0';
          app.style.transform = 'translateY(-100%)';
          setTimeout(() => {
            const resultStyle = document.getElementById('result-style');
            if (resultStyle) resultStyle.remove();
            const resultScript = document.getElementById('result-script');
            if (resultScript) resultScript.remove();
            const taskData = window.task11Data;
            if (!taskData) {
              alert('Ошибка: исходное задание не найдено');
              return;
            }
            const taskStyle = document.createElement('style');
            taskStyle.id = 'task11-style';
            taskStyle.textContent = taskData.css || '';
            document.head.appendChild(taskStyle);
            app.className = 'task-container';
            app.innerHTML = taskData.html || '';
            const taskScript = document.createElement('script');
            taskScript.id = 'task11-script';
            taskScript.textContent = taskData.js || '';
            document.body.appendChild(taskScript);
            setTimeout(() => {
              const gen = document.getElementById('genBtn');
              if (gen && window.generateFields) gen.addEventListener('click', window.generateFields);
              const comp = document.getElementById('computeBtn');
              if (comp && window.compute) comp.addEventListener('click', window.compute);
              const menu = document.getElementById('toMenuBtn');
              if (menu && window.backToMenu) menu.addEventListener('click', window.backToMenu);
              const n = document.getElementById('n');
              if (n) n.focus();
            }, 100);
            app.style.opacity = '1';
            app.style.transform = 'translateY(0)';
            app.style.transition = '';
          }, 500);
        };
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', function(){
            const b = document.getElementById('backToInputBtn');
            if (b) b.addEventListener('click', window.backToInput);
            const m = document.getElementById('toMenuBtn');
            if (m) m.addEventListener('click', window.backToMenu);
          });
        } else {
          const b = document.getElementById('backToInputBtn');
          if (b) b.addEventListener('click', window.backToInput);
          const m = document.getElementById('toMenuBtn');
          if (m) m.addEventListener('click', window.backToMenu);
        }
        window.backToMenu = async function() {
          try {
            const responseStr = await pywebview.api.backToMain();
            const data = JSON.parse(responseStr);
            const app = document.getElementById('app') || document.body;
            const oldStyle = document.getElementById('result-style') || document.getElementById('main-style');
            if (oldStyle) oldStyle.remove();
            const oldScript = document.getElementById('result-script') || document.getElementById('main-script');
            if (oldScript) oldScript.remove();
            if (data.css) {
              const style = document.createElement('style');
              style.id = 'main-style';
              style.textContent = data.css;
              document.head.appendChild(style);
            }
            app.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            app.style.opacity = '0';
            app.style.transform = 'translateY(20px)';
            setTimeout(() => {
              app.replaceChildren();
              app.innerHTML = data.html || '';
              app.className = 'container';
              if (data.js) {
                const script = document.createElement('script');
                script.id = 'main-script';
                script.textContent = data.js;
                document.body.appendChild(script);
              }
              app.style.transform = 'translateY(-20px)';
              app.offsetHeight;
              app.style.opacity = '1';
              app.style.transform = 'translateY(0)';
              if (typeof attachHandlers === 'function') setTimeout(attachHandlers, 50);
            }, 500);
          } catch (e) {
            window.showError('Ошибка при возврате в меню: ' + (e && e.message ? e.message : String(e)));
          }
        };
      })();
    </script>
  </body>
</html>
'''

FILE_CONTENTS = {
    'main.txt': main_txt,
    'main.py': main_py,
    'task1.txt': task1_txt,
    'task1_result.txt': task1_result_txt,
    'task2.txt': task2_txt,
    'task2_result.txt': task2_result_txt,
    'task3.txt': task3_txt,
    'task3_result.txt': task3_result_txt,
    'task4.txt': task4_txt,
    'task4_result.txt': task4_result_txt,
    'task5.txt': task5_txt,
    'task5_result.txt': task5_result_txt,
    'task6.txt': task6_txt,
    'task6_result.txt': task6_result_txt,
    'task7.txt': task7_txt,
    'task7_result.txt': task7_result_txt,
    'task8.txt': task8_txt,
    'task8_result.txt': task8_result_txt,
    'task9.txt': task9_txt,
    'task9_result.txt': task9_result_txt,
    'task10.txt': task10_txt,
    'task10_result.txt': task10_result_txt,
    'task11.txt': task11_txt,
    'task11_result.txt': task11_result_txt,
}


def is_valid_html(content: str) -> bool:
    if len(content.strip()) < 100:
        return False
    content = content.strip()
    return content.startswith('<html') and content.endswith('</html>')


def is_valid_python(content: str, filename: str) -> bool:
    try:
        exec_globals = {'__file__': filename}
        compile(content, filename, 'exec')
        exec(content, exec_globals)
        return True
    except Exception as e:
        print(f"Error in {filename}: {e}", file=sys.stderr)
        return False


def check_and_recreate():
    files_to_check = list(FILE_CONTENTS.keys())
    recreated = []
    for filename in files_to_check:
        if not os.path.exists(filename):
            print(f"Файл {filename} не существует. Пересоздаю...")
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(FILE_CONTENTS[filename])
            recreated.append(filename)
            continue

        with open(filename, 'r', encoding='utf-8') as f:
            current_content = f.read()

        is_valid = False
        if filename == 'main.py':
            is_valid = is_valid_python(current_content, filename)
        else:
            is_valid = is_valid_html(current_content)

        if not is_valid:
            print(f"Файл {filename} поврежден. Пересоздаю...")
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(FILE_CONTENTS[filename])
            recreated.append(filename)

    if recreated:
        print(f"Пересозданы файлы: {', '.join(recreated)}")
    else:
        print("Все файлы в порядке.")


if __name__ == '__main__':
    check_and_recreate()
