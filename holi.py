from flask import Flask

app = Flask(__name__)

@app.route('/')
def holi_page():
    return '''
    <html>
    <head>
        <title>Happy Holi!</title>
        <style>
            body {
                background: linear-gradient(to right, #ff9a9e, #fad0c4);
                text-align: center;
                font-family: Arial, sans-serif;
                overflow: hidden;
            }
            h1 {
                color: #fff;
                font-size: 60px;
                margin-top: 15%;
                display: inline-block;1
                animation: flip 2s infinite, glow 1.5s alternate infinite;
                text-shadow: 0 0 10px #ff6600, 0 0 20px #ff4500, 0 0 30px #ff0000;
            }
            p {
                color: #fff;
                font-size: 22px;
                text-shadow: 0 0 10px #990099, 0 0 20px #ff00ff;
            }
            .color-drop {
                position: absolute;
                width: 15px;
                height: 15px;
                background-color: red;
                border-radius: 50%;
                opacity: 0.9;
                animation: fall 2.5s linear infinite;
            }
            .image-drop {
                position: absolute;
                width: 70px;
                height: 70px;
                background-size: cover;
                background-repeat: no-repeat;
                border-radius: 50%;
                animation: fall 3.5s linear infinite;
            }
            @keyframes fall {
                0% { transform: translateY(-10px); opacity: 1; }
                100% { transform: translateY(100vh); opacity: 0; }
            }
            @keyframes flip {
                0% { transform: rotateY(0deg); }
                50% { transform: rotateY(180deg); }
                100% { transform: rotateY(360deg); }
            }
            @keyframes glow {
                from { text-shadow: 0 0 10px #ff6600, 0 0 20px #ff4500, 0 0 30px #ff0000; }
                to { text-shadow: 0 0 20px #ffcc00, 0 0 30px #ff9900, 0 0 40px #ff6600; }
            }
        </style>
        <script>
            document.addEventListener("click", function() {
                for (let i = 0; i < 50; i++) {
                    let drop = document.createElement("div");
                    drop.className = "color-drop";
                    drop.style.backgroundColor = getRandomColor();
                    drop.style.left = Math.random() * window.innerWidth + "px";
                    drop.style.top = Math.random() * -50 + "px";
                    drop.style.animationDuration = (Math.random() * 2 + 1.5) + "s";
                    document.body.appendChild(drop);
                    setTimeout(() => drop.remove(), 2500);
                }
                for (let i = 0; i < 15; i++) {
                    let imgDrop = document.createElement("div");
                    imgDrop.className = "image-drop";
                    imgDrop.style.backgroundImage = "url('https://upload.wikimedia.org/wikipedia/commons/3/3a/Holi_Festival_in_India.png')";
                    imgDrop.style.left = Math.random() * window.innerWidth + "px";
                    imgDrop.style.top = Math.random() * -50 + "px";
                    imgDrop.style.animationDuration = (Math.random() * 3 + 2) + "s";
                    document.body.appendChild(imgDrop);
                    setTimeout(() => imgDrop.remove(), 4000);
                }
            });

            function getRandomColor() {
                let letters = '0123456789ABCDEF';
                let color = '#';
                for (let i = 0; i < 6; i++) {
                    color += letters[Math.floor(Math.random() * 16)];
                }
                return color;
            }
        </script>
    </head>
    <body>
        <h1>Happy Holi!</h1>
        <p>Click anywhere to make colors and images rain!</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
#11
