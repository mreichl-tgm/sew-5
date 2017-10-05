package persistence

import util.PersistenceUtil

interface IRepository<T> {
    fun persist(item: T): Boolean {
        val entityManager = PersistenceUtil.getEntityManager()

        try {
            entityManager.transaction.begin()
            entityManager.persist(item)
            entityManager.transaction.commit()
        } catch (e: Exception) {
            return false
        }

        entityManager.close()
        return true
    }

    fun merge(item: T): Boolean {
        val entityManager = PersistenceUtil.getEntityManager()

        try {
            entityManager.transaction.begin()
            entityManager.merge(item)
            entityManager.transaction.commit()
        } catch (e: Exception) {
            return false
        }

        entityManager.close()
        return true
    }

    fun remove(item: T): Boolean {
        val entityManager = PersistenceUtil.getEntityManager()

        try {
            entityManager.transaction.begin()
            entityManager.remove(item)
            entityManager.transaction.commit()
        } catch (e: Exception) {
            return false
        }

        entityManager.close()
        return true
    }

    fun find(id: Long): T?

    fun findAll(): List<T>
}