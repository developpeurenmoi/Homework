const getRandomHexaColor = () => {
    const hexa = '0123456789abcdef';
    let hexaCode = "#";
    for (let i = 0; i < 6; i++) {
        hexaCode += hexa[Math.floor(Math.random() * 16)]
    }
    return hexaCode
};

setInterval(() => {
    document.querySelector('body').style.backgroundColor =
        getRandomHexaColor();
}, 100);

const getCurrentTime = () => {
    const date = new Date();
    yy = (date.getFullYear()) + '년 ',
    mm = date.getMonth() + 1
    mm = (mm <10?'0':'') + mm +'월 ',
    dd= (date.getDate()<10?'0':'') + date.getDate() +'일 ',
    h = (date.getHours()<10?'0':'') + date.getHours() +'시 ',
    m = (date.getMinutes()<10?'0':'') + date.getMinutes() + '분 '
    s = (date.getSeconds()<10?'0':'') + date.getSeconds() + '초 '
    
    console.log(date);

    document.querySelector('.now').innerHTML = yy + mm + dd + h + m + s;
};

const initClock = () => {
    getCurrentTime();
    setInterval(getCurrentTime, 1000);
};

initClock();