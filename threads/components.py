from sourcetypes import django_html
from sourcetypes import javascript
from tetra import Component
from tetra import Library
from tetra import public
from threads.models import Comment as CommentModel
from threads.models import Thread as ThreadModel


default = Library()


@default.register
class ThreadItem(Component):
  def load(self, thread, index=None):
    self.thread = thread
    self.index = index

  template: django_html = """
  <div class="flex pv2">
    {% if index %}
      <div class="pr1">
        {{ index }}.
      </div>
    {% endif %}

    <a href="/thread/{{thread.pk}}" class="no-underline">
      {{ thread.name }}
    </a>
  </div>
  """


@default.register
class Feed(Component):
  def load(self):
    self.threads = ThreadModel.objects.all()

  template: django_html = """
  <div class="flex flex-column">
    <div class="tr">
      <a href="/create" class="no-underline">
        Create Thread
      </a>
    </div>

    {% for thread in threads %}
      {% @ thread_item thread=thread index=forloop.counter / %}
    {% endfor %}
  </div>
  """


@default.register
class Thread(Component):
  def load(self, thread):
    self.thread = thread

  template: django_html = """
  <h3>
    {{thread.name}}
  </h3>

  {% if thread.description %}
    <p>
      {{thread.description}}
    </p>
  {% endif %}

  {% @ comment_item thread=thread / %}

  <hr />

  {% for comment in thread.top_level_comments.all %}
    {% @ comment_item comment=comment / %}
  {% endfor %}
  """

@default.register
class CommentItem(Component):
  text = public(None)

  def load(self, comment=None, thread=None):
    self.thread = thread
    self.comment = comment

  @public
  def handle_create(self):
    if self.text:
      CommentModel.objects.create(
        text=self.text,
        post_parent=self.thread,
        comment_parent=self.comment)

    # TODO: This seems to re-render the whole comment subtree. That isn't strictly
    # necessary, use some client callback to patch the interface maybe?

  template: django_html = """
  <div>
    {% if comment %}
      <p>
        {{comment.text}}
      </p>
    {% endif %}

    <div>
      <a x-show="!reply" @click="reply = true" class="black-40">
        <small>
          Reply
        </small>
      </a>
    </div>

    <form
      x-show="reply"
      @submit.prevent="onReplySubmit()"
    >
      <textarea
        class="w-100"
        x-model="text"
      >
      </textarea>

      <div class="tr">
        <button @click="resetReply()">
          Cancel
        </button>

        <button type="submit">
          Submit
        </button>
      </div>
    </form>

    {% if comment %}
      <div class="flex flex-column pl4 bl bw1 b--black-10">
        {% for nested_comment in comment.nested_comments.all %}
          {% @ comment_item comment=nested_comment / %}
        {% endfor %}
      </div>
    {% endif %}
  </div>
  """

  script: javascript = """
  export default {
    reply: false,

    onReplySubmit() {
      this.handle_create()
        .catch(() => alert('Something went Wrong'))
        .finally(() => this.resetReply())
    },

    resetReply() {
      this.reply = false
      this.text = null
    }
  }
  """

@default.register
class CreateThread(Component):
  name = public(None)
  description = public(None)

  @public
  def handle_submit(self):
    if self.name:
      ThreadModel.objects.create(name=self.name, description=self.description or None)

    # TODO: Gotta redirect after creating the instance. Is there a client callback for
    # that?

  template: django_html = """
  <div>
    <h3>
      Create a Thread
    </h3>

    <form @submit.prevent="onSubmit()">
      <input
          x-model="name"
          placeholder="Name"
          class="w-100 border-box"
      />

      <textarea
        x-model="description"
        class="w-100 mt3"
        placeholder="Description"
        rows="12"
      ></textarea>

      <div class="tr">
        <button>
          Cancel
        </button>

        <button type="submit">
          Submit
        </button>
      </div>
    </form>
  </div>
  """

  script: javascript = """
  export default {
    onSubmit() {
      this.handle_submit()
    },
  }
  """
