<script lang="ts">
	import { goto } from '$app/navigation';

	var brain = '/brain.jpg';

	const handleLoginClick = () => {
		goto('/login');
	};

	const handleSignUpClick = () => {
		goto('signup');
	};
</script>

<div
	class="
		h-screen w-screen
		bg-slate-200
"
>
	<h2
		class="
			absolute top-20 left-20
			text-6xl
			font-light
			"
	>
		Insert Company Slogan Here
	</h2>

	<div
		class="flex flex-row justify-center items-center
				h-full w-6/12
				"
	>
		<button
			on:click={handleSignUpClick}
			class="
				h-12 w-40
				bg-sky-300/100
				border-white border-solid rounded-lg
				hover:bg-sky-400/100
				m-6
				"
		>
			Sign Up
		</button>
		<button
			on:click={handleLoginClick}
			class="
				h-12 w-40
				border-slate-500 border-solid border-2 rounded-lg
				hover:bg-slate-300
				"
		>
			Login
		</button>
	</div>
</div>
