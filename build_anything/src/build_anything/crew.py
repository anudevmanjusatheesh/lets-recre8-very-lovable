from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from langchain_community.agent_toolkits.file_management.toolkit import FileManagementToolkit
from build_anything.tools.file_tools import FileTools
from crewai.memory import LongTermMemory, ShortTermMemory, EntityMemory
# from crewai.memory.storage import LTMSQLiteStorage, RAGStorage
from crewai.memory.storage.rag_storage import RAGStorage
from crewai.memory.storage.ltm_sqlite_storage import LTMSQLiteStorage
from typing import List, Optional

# Uncomment the following line to use an example of a custom tool
# from build_anything.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

# coder = LLM(
# 		# api_key=os.getenv("GROQ_API_KEY"),
# 		# model="anthropic/claude-3-7-sonnet-20250219",
#   		model="anthropic/claude-3-5-sonnet-20241022"
# 	)
coder = LLM(model="openai/o3-mini-2025-01-31")

@CrewBase
class BuildAnythingCrew():
	"""BuildAnything crew"""

	toolkit = FileManagementToolkit(
      root_dir='/mnt/c/Projects/playground/lovable_clone/files',
      selected_tools=["read_file", "list_directory"]
    )

	@agent
	def task_breakdown_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['task_breakdown_agent'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True,
   			allow_delegation=True,
			
		)

	@agent
	def backend_developer(self) -> Agent:
		return Agent(
			config=self.agents_config['backend_developer'],
			# tools= [FileTools.write_file], 
			# tools = self.toolkit.get_tools(),
			verbose=True,
			llm = coder
		)

	@agent
	def html_developer(self) -> Agent:
		return Agent(
			config=self.agents_config['html_developer'],
			# tools= [FileTools.write_file]+self.toolkit.get_tools(), 
			verbose=True,
			llm = coder,
   			respect_context_window = False,
		)
	@agent
	def css_developer(self) -> Agent:
		return Agent(
			config=self.agents_config['css_developer'],
			# tools= [FileTools.write_file]+self.toolkit.get_tools(), 
			verbose=True,
			llm = coder,
			respect_context_window = False
			)
	@agent
	def js_developer(self) -> Agent:
		return Agent(
			config=self.agents_config['js_developer'],
			# tools= [FileTools.write_file]+self.toolkit.get_tools(), 
			verbose=True,
			llm = coder
		)

	@task
	def project_planning_task(self) -> Task:
		return Task(
			config=self.tasks_config['project_planning_task'],
		)

	@task
	def backend_development_task(self) -> Task:
		return Task(
			config=self.tasks_config['backend_development_task'],
			output_file='server.js'
		)

	@task
	def html_development_task(self) -> Task:
		return Task(
			config=self.tasks_config['html_development_task'],
			output_file='index.html'
		)
	@task
	def css_development_task(self) -> Task:
		return Task(
			config=self.tasks_config['css_development_task'],
			output_file='styles.css'
		)
	@task
	def js_development_task(self) -> Task:
		return Task(
			config=self.tasks_config['js_development_task'],
			output_file='scripts.js'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the BuildAnything crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/

 			memory = True,
    # Long-term memory for persistent storage across sessions
			long_term_memory = LongTermMemory(
				storage=LTMSQLiteStorage(
					db_path="./my_crew1/long_term_memory_storage.db"
				)
			),
			# Short-term memory for current context using RAG
			short_term_memory = ShortTermMemory(
				storage = RAGStorage(
						embedder_config={
							"provider": "openai",
							"config": {
								"model": 'text-embedding-3-small'
							}
						},
						type="short_term",
						path="./my_crew1/short/"
					)
				),
			# Entity memory for tracking key information about entities
			entity_memory = EntityMemory(
				storage=RAGStorage(
					embedder_config={
						"provider": "openai",
						"config": {
							"model": 'text-embedding-3-small'
						}
					},
					type="short_term",
					path="./my_crew1/key_info/"
				)
			),
		)