
			// Establish WebSocket connection
			const chatSocket = new WebSocket("ws://" + window.location.host + "/");
			
			// When connection is opened, log success message
			chatSocket.onopen = () => console.log("Connection established.");
		  
			// When connection is closed unexpectedly, log error message
			chatSocket.onclose = () => console.log("Connection closed unexpectedly.");
		  
			// Focus on message input field when page loads
			document.querySelector("#message").focus();
		  
			// Send message when Enter key is pressed
			document.querySelector("#message").onkeyup = (e) => {
			  if (e.keyCode === 13) {
				document.querySelector("#id_message_send_button").click();
			  }
			};
		  
			// Send message when send button is clicked
			document.querySelector("#id_message_send_button").onclick = () => {
				const messageInput = document.querySelector("#message").value;
				chatSocket.send(JSON.stringify({ 
					message: messageInput, 
					username: "{{user.username}}" ,
					frienduname:"{{friend.username}}"
				}));
			};
		  
			// Display received messages
			chatSocket.onmessage = (e) => {
				const { username, message,frienduname,time} = JSON.parse(e.data);

				const messageContainer = document.createElement("div");
				//# Assign the value of x based on the condition
				
    			

				// Create the image container
    			const imgContainer = document.createElement("div");
    			imgContainer.classList.add("img_cont_msg");

				const img = document.createElement("img");
    			
    			img.classList.add("rounded-circle", "user_img_msg");

				// Append the image to the image container
    			

				// Create the message container
				const msgContainer = document.createElement("div");
				msgContainer.classList.add("msg_cotainer");
				msgContainer.textContent = `${message}`;
				// Create the timestamp element
				const timestamp = document.createElement("span");
				timestamp.classList.add("msg_time");
				timestamp.textContent = time; // Use the date provided by the server

				// Append the timestamp to the message container
				msgContainer.appendChild(timestamp);
				if(username=="{{friend.username}}"){
					img.src = "{{ frnd_obj.image.url }}";
					imgContainer.appendChild(img);
					messageContainer.classList.add("d-flex", "justify-content-start", "mb-4");
					messageContainer.appendChild(imgContainer);
					messageContainer.appendChild(msgContainer);
				}
				else{
					img.src = "{{ user_obj.image.url }}";
					imgContainer.appendChild(img);
					messageContainer.classList.add("d-flex", "justify-content-end", "mb-4");
					messageContainer.appendChild(msgContainer);
					messageContainer.appendChild(imgContainer);
					
				}
				// Append the image container and message container to the message container
				document.querySelector("#message").value = "";
				// Append the new message container to the display area
    			document.querySelector("#display").appendChild(messageContainer);
				scrollToBottom();
			};
			function scrollToBottom() {
				const display = document.querySelector("#display");
				display.scrollTop = display.scrollHeight;
			}
			window.onload = () => {
				scrollToBottom();
			};
