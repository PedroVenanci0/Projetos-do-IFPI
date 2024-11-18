var Hotel = /** @class */ (function () {
    function Hotel(quantReservas) {
        if (quantReservas === void 0) { quantReservas = 0; }
        this.quantReservas = quantReservas;
    }
    Hotel.prototype.adicionarReserva = function () {
        this.quantReservas++;
    };
    return Hotel;
}());
var hotel = new Hotel(2);
console.log(hotel.quantReservas);
