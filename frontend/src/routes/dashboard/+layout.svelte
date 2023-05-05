<script lang="ts">
	import Navbar from '../../components/navbar.svelte';
</script>

<nav
	class="fixed z-10 w-full bg-white bg-opacity-70 backdrop-blur sm:md:backdrop-filter-none navbar peer-checked:navbar-active md:absolute md:bg-transparent"
>
	<div class="m-auto md:px-20">
		<div class="flex flex-wrap items-center justify-between gap-6 md:py-3 md:gap-0">
			<div class="w-full px-5 flex justify-between lg:w-max md:px-0">
				<a href="/" aria-label="logo" class="flex items-center">
					<div>
						<p class="text-4xl font-bold text-red-500">sumitup.</p>
					</div>
				</a>
				<label
					id="nice"
					for="hbr"
					class="peer-checked:hamburger block relative z-20 p-6 -mr-6 cursor-pointer lg:hidden"
				>
					<div
						aria-hidden="true"
						class="m-auto h-0.5 w-6 rounded bg-red-500 transition duration-300"
					/>
					<div
						aria-hidden="true"
						class="m-auto mt-2 h-0.5 w-6 rounded bg-red-500 transition duration-300"
					/>
				</label>
			</div>
			<div
				id="menu"
				class="navmenu backdrop-filter-none hidden w-full flex-wrap justify-end items-center mb-16 mx-6 space-y-20 p-6 rounded-xl shadow-lg bg-white lg:space-y-0 lg:p-0 lg:m-0 lg:flex md:flex-nowrap lg:bg-transparent lg:w-7/12 lg:shadow-none"
			>
				<div class="text-gray-600 lg:pr-4">
					<ul class="space-y-6 tracking-wide font-medium text-lg lg:text-sm lg:flex lg:space-y-0">
						<li class="pr-3">
							<button
								id="dropdownNavbarLink"
								data-dropdown-toggle="dropdownNavbar"
								class="flex justify-between items-center py-2 pr-4 pl-3 w-full font-bold text-gray-700 border-b border-gray-100 hover:bg-gray-50 md:hover:bg-transparent md:border-0 md:hover:text-red-700 md:p-0 md:w-auto"
								>About</button
							>
							<div
								id="dropdownNavbar"
								class="hidden z-10 w-44 font-normal bg-white rounded divide-y divide-gray-100 shadow"
							>
								<ul class="py-1 text-sm text-gray-700" aria-labelledby="dropdownLargeButton">
									<li>
										<a href="/" class="block py-2 px-4 hover:bg-gray-100">Institutions</a>
									</li>
									<li>
										<a href="/" class="block py-2 px-4 hover:bg-gray-100">Patients</a>
									</li>
								</ul>
							</div>
						</li>
					</ul>
				</div>
				<div
					class="w-full text-white sm:px-6 font-bold space-y-2 flex flex-colsm:flex-row lg:space-y-2 md:w-max lg:border-l"
				>
					<a
						href="/audiocreate"
						type="button"
						title="Start buying"
						class="w-full py-2.5 px-3 text-center rounded-xl transition bg-red-500 border-2 border-red-500 sm:w-max"
					>
						<span class="block text-white font-bold lg:text-sm"> Upload Meeting </span></a
					>
				</div>

				<div
					class="w-full text-white sm:pl-6 font-bold space-y-2 flex flex-colsm:flex-row lg:space-y-2 md:w-max lg:border-l"
				>
					<a
						href="/logout"
						type="button"
						title="Start buying"
						class="w-full py-2.5 px-3 text-center text-red-500 rounded-xl transition border-2 border-red-500 sm:w-max"
					>
						<span class="block font-bold lg:text-sm"> Logout </span></a
					>
				</div>
				<div
					class="w-full text-white sm:pl-6 font-bold space-y-2 flex flex-colsm:flex-row lg:space-y-2 md:w-max lg:border-l"
				>
					<a
						href="/signup"
						type="button"
						title="Start buying"
						class="w-full py-2.5 px-3 text-center rounded-xl transition bg-red-500 sm:w-max"
					>
						<span class="block text-white font-bold lg:text-sm"> Register </span></a
					>
				</div>
			</div>
		</div>
	</div>
</nav>

<slot />
