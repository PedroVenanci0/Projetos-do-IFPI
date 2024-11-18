class Radio {
    volume: number;
  
    constructor(volume: number = 0) {
      this.volume = volume;
    }
  }
  
  let r: Radio = new Radio(); // 0
  r.volume = 10; 
  console.log(r.volume); 
  