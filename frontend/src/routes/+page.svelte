<script lang="ts">
	import { goto } from '$app/navigation';

	const handleLoginClick = () => {
		goto('/login');
	};

	const handleSignUpClick = () => {
		goto('signup');
	};
</script>

<h2
	class="
        bg-slate-200
        absolute top-20 left-20
        text-6xl
        font-light
        "
>
	Insert Company Slogan Here
</h2>

<div
	class="flex flex-row justify-center items-center
            h-screen bg-slate-200"
>
	<button
		on:click={handleLoginClick}
		class="
            h-12 w-40
            bg-sky-300/100
            border-white border-solid rounded-lg
            hover:bg-sky-400/100
            m-6"
	>
		Login
	</button>
	<button
		on:click={handleSignUpClick}
		class="
            h-12 w-40
            border-slate-500 border-solid border-2 rounded-lg
            hover:bg-slate-300
            "
	>
		Sign Up
	</button>
</div>
