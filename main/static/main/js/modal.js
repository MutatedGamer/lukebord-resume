function showModal(img) {
	var modal = document.getElementById(img.id + '-modal');
	var modalImg =  modal.getElementsByClassName("modal-content")[0];
	// console.log(modalImg);
	// var modalCaption = modal.getElementsByClassName("caption")[0];
	// console.log(modalCaption);
	// console.log(modal);
	
	modal.style.display = "flex";
	modalImg.src = img.src;
    // modalCaption.innerHTML = img.alt;
    // Get the <span> element that closes the modal
	var span = modal.getElementsByClassName("close")[0];

	// When the user clicks on <span> (x) or the modal itself, close the modal
	span.onclick = function() { 
	  modal.style.display = "none";
	}

	modal.onclick = function() { 
	  modal.style.display = "none";
	}
}