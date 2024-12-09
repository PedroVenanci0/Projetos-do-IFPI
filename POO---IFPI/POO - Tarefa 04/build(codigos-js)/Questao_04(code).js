var Radio = /** @class */ (function () {
    function Radio(volume) {
        if (volume === void 0) { volume = 0; }
        this.volume = volume;
    }
    return Radio;
}());
var r = new Radio(); // 0
r.volume = 10;
console.log(r.volume);
