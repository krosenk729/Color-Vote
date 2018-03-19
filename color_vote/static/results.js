$(document).ready(function(){
	let canvases = $('canvas');
	for(let c of canvases){
		let _color = $(c),
			_red = color.attr('data-red'),
			_green = color.attr('data-green'),
			_blue = color.attr('data-blue'), 
			ctx = color.getContext('2d');
		let myChart = new Chart(ctx, {
			type: 'horizontalBar',
			data: {
				labels: ['red', 'green', 'blue'],
				datasets: [{
					backgroundColor: ['#E91E63', '#4CAF50', '#03A9F4'],
					data: [_red, _green, _blue]
				}]
			},
			options: {
				responsive: true,
				scales: {
					xAxis: [{
						ticks: {
							// beginAtZero: true
							min: 0,
							max: 255
						}
					}]
				}
			}
		});
	}
});