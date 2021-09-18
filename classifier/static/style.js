 /* 1. input#userInput 의 'input' 이벤트 때, */
 const button = document.querySelector('button');
 const userInput = document.querySelector('#userInput');
 button.addEventListener('click', event => {
     axios.get(`clf/${userInput.value}`, {
     }).then((res) => {
         let ratio = res.data.value;
         console.log(ratio)
         if (ratio === -1) swal("", "좀 더 긴 문장을 입력해주세요.")
         else if (ratio <= 50) {
            ratio = 100 - ratio
            swal("", `해당 문장은 남성에 더 가깝습니다.(${ratio}%) `);
         }
         else{
            swal("", `해당 문장은 여성에 더 가깝습니다.(${ratio}%) `);
         }
     })
 });